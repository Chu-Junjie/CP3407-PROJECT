import re
import sqlite3
from pathlib import Path
from typing import Any

import pandas as pd
from flask import Flask, jsonify, request


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "US-02 Database Setup & Import.csv"
DB_PATH = BASE_DIR / "digital_products.db"
TABLE_NAME = "products"

app = Flask(__name__)


# ============================================================
# DATABASE
# ============================================================

def get_connection() -> sqlite3.Connection:
    """Return a SQLite connection whose rows can be accessed by column name."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def setup_database() -> int:
    """Create or reuse the products table and return its row count."""
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Missing dataset: {CSV_PATH.name}")

    with get_connection() as connection:
        table_exists = connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = ?",
            (TABLE_NAME,),
        ).fetchone()[0]

        if table_exists:
            row_count = connection.execute(
                f"SELECT COUNT(*) FROM {TABLE_NAME}"
            ).fetchone()[0]
            if row_count > 0:
                return int(row_count)

        dataframe = pd.read_csv(CSV_PATH)

        required_columns = {
            "ProductID",
            "ProductCategory",
            "ProductBrand",
            "ProductPrice",
            "CustomerAge",
            "CustomerGender",
            "PurchaseFrequency",
            "CustomerSatisfaction",
            "PurchaseIntent",
        }
        missing_columns = required_columns.difference(dataframe.columns)
        if missing_columns:
            missing_text = ", ".join(sorted(missing_columns))
            raise ValueError(f"Dataset is missing required columns: {missing_text}")

        dataframe.to_sql(TABLE_NAME, connection, if_exists="replace", index=False)
        connection.commit()
        return int(len(dataframe))


# ============================================================
# REQUEST AND NATURAL-LANGUAGE PROCESSING
# ============================================================

def parse_budget_from_text(text: str | None) -> float | None:
    """Extract a budget such as '$1,500', 'under 900', or 'budget 1200'."""
    if not text:
        return None

    normalised = str(text).lower().replace(",", "")
    patterns = [
        r"(?:under|below|less\s+than|budget(?:\s+(?:of|is))?|around|up\s+to|maximum|max|limit(?:\s+is)?)\s*\$?\s*(\d+(?:\.\d+)?)",
        r"\$\s*(\d+(?:\.\d+)?)",
    ]

    for pattern in patterns:
        match = re.search(pattern, normalised)
        if match:
            return float(match.group(1))

    return None


def _normalise_optional_text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def read_request_filters() -> dict[str, Any]:
    """Read recommendation filters from GET parameters or POST JSON."""
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
    else:
        payload = request.args

    # 'intent' is accepted for compatibility with earlier Week 7 test examples.
    query_text = str(payload.get("query") or payload.get("intent") or "").strip()
    category = _normalise_optional_text(payload.get("category"))
    brand = _normalise_optional_text(payload.get("brand"))

    max_price = payload.get("max_price")
    try:
        budget = float(max_price) if max_price not in (None, "") else None
    except (TypeError, ValueError):
        budget = None

    if budget is None:
        budget = parse_budget_from_text(query_text)

    if budget is not None and budget < 0:
        budget = None

    return {
        "query": query_text,
        "category": category,
        "brand": brand,
        "budget": budget,
    }


# ============================================================
# RECOMMENDATION ENGINE
# ============================================================

def fetch_candidate_products(filters: dict[str, Any]) -> list[dict[str, Any]]:
    """Return database candidates that satisfy strict category and budget filters."""
    where_clauses: list[str] = []
    params: list[Any] = []

    if filters.get("category"):
        where_clauses.append("ProductCategory = ?")
        params.append(filters["category"])

    # The UI describes this as a maximum budget, so no result may exceed it.
    if filters.get("budget") is not None:
        where_clauses.append("ProductPrice <= ?")
        params.append(float(filters["budget"]))

    where_sql = f"WHERE {' AND '.join(where_clauses)}" if where_clauses else ""

    sql = f"""
        SELECT
            ProductID,
            ProductCategory,
            ProductBrand,
            ProductPrice,
            CustomerAge,
            CustomerGender,
            PurchaseFrequency,
            CustomerSatisfaction,
            PurchaseIntent
        FROM {TABLE_NAME}
        {where_sql}
        ORDER BY ProductPrice ASC
    """

    with get_connection() as connection:
        rows = connection.execute(sql, params).fetchall()

    return [dict(row) for row in rows]


def calculate_match_score(
    product: dict[str, Any], filters: dict[str, Any]
) -> tuple[int, list[str]]:
    """Calculate a score from 0 to 100 and return short explanation reasons."""
    score = 8
    reasons: list[str] = []

    category = filters.get("category")
    if category:
        if product["ProductCategory"] == category:
            score += 22
            reasons.append(f"matches category: {category}")
        else:
            score -= 15

    brand = filters.get("brand")
    if brand:
        if product["ProductBrand"] == brand:
            score += 22
            reasons.append(f"matches brand: {brand}")
        else:
            score -= 8

    budget = filters.get("budget")
    if budget is not None:
        price = float(product["ProductPrice"])
        budget_value = float(budget)

        if budget_value > 0 and price <= budget_value:
            price_ratio = price / budget_value
            ideal_ratio = 0.70
            price_score = round(18 - abs(price_ratio - ideal_ratio) * 24)
            price_score = max(6, min(18, price_score))
            score += price_score
            reasons.append(f"within budget ${budget_value:.0f}")

    satisfaction = int(product["CustomerSatisfaction"])
    score += satisfaction * 2
    if satisfaction >= 4:
        reasons.append("high customer satisfaction")

    purchase_frequency = int(product["PurchaseFrequency"])
    if purchase_frequency >= 7:
        score += 4
        reasons.append("strong purchase frequency")
    elif purchase_frequency >= 4:
        score += 2

    if int(product["PurchaseIntent"]) == 1:
        score += 4
        reasons.append("positive purchase intent")

    return max(0, min(100, int(score))), reasons[:4]


def build_leaderboard(
    filters: dict[str, Any], limit: int = 5
) -> list[dict[str, Any]]:
    """Build and sort the recommendation leaderboard."""
    setup_database()
    candidates = fetch_candidate_products(filters)

    leaderboard: list[dict[str, Any]] = []
    for product in candidates:
        score, reasons = calculate_match_score(product, filters)
        product_name = (
            f"{product['ProductBrand']} {product['ProductCategory']} "
            f"#{product['ProductID']}"
        )

        leaderboard.append(
            {
                "product_id": int(product["ProductID"]),
                "product_name": product_name,
                "name": product_name,
                "category": product["ProductCategory"],
                "brand": product["ProductBrand"],
                "price": round(float(product["ProductPrice"]), 2),
                "match_score": score,
                "reason": "; ".join(reasons) or "general product match",
            }
        )

    leaderboard.sort(
        key=lambda item: (item["match_score"], -item["price"]),
        reverse=True,
    )
    return leaderboard[: max(0, int(limit))]


# ============================================================
# FLASK API
# ============================================================

@app.route("/api/health", methods=["GET"])
def health_check():
    row_count = setup_database()
    return jsonify(
        {
            "status": "success",
            "database": DB_PATH.name,
            "table": TABLE_NAME,
            "records": row_count,
        }
    )


@app.route("/api/products", methods=["GET"])
def products():
    setup_database()

    with get_connection() as connection:
        rows = connection.execute(
            f"""
            SELECT ProductID, ProductCategory, ProductBrand, ProductPrice
            FROM {TABLE_NAME}
            ORDER BY ProductPrice ASC
            LIMIT 5
            """
        ).fetchall()

    return jsonify(
        {
            "status": "success",
            "data": [dict(row) for row in rows],
        }
    )


@app.route("/api/recommend", methods=["GET", "POST"])
def recommend():
    filters = read_request_filters()
    leaderboard = build_leaderboard(filters, limit=5)

    return jsonify(
        {
            "status": "success",
            "filters": filters,
            "data": leaderboard,
        }
    )


@app.errorhandler(FileNotFoundError)
def handle_missing_file(error: FileNotFoundError):
    return jsonify({"status": "error", "message": str(error)}), 500


@app.errorhandler(ValueError)
def handle_invalid_dataset(error: ValueError):
    return jsonify({"status": "error", "message": str(error)}), 500


if __name__ == "__main__":
    print("Starting backend API server at http://127.0.0.1:5000")
    print("Health check: http://127.0.0.1:5000/api/health")
    app.run(debug=True, port=5000)
