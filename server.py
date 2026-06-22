import os
import re
import sqlite3
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, request


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "US-02 Database Setup & Import.csv"
DB_PATH = BASE_DIR / "digital_products.db"
TABLE_NAME = "products"

app = Flask(__name__)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def setup_database():
    """Create the SQLite product table from CSV if the database is missing or empty."""
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Missing dataset: {CSV_PATH.name}")

    with get_connection() as connection:
        table_exists = connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = ?",
            (TABLE_NAME,),
        ).fetchone()[0]

        if table_exists:
            row_count = connection.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}").fetchone()[0]
            if row_count > 0:
                return row_count

        dataframe = pd.read_csv(CSV_PATH)
        dataframe.to_sql(TABLE_NAME, connection, if_exists="replace", index=False)
        connection.commit()
        return len(dataframe)


def parse_budget_from_text(text):
    match = re.search(r"(?:under|below|less than|budget|around)?\s*\$?\s*(\d{3,5})", text.lower())
    return float(match.group(1)) if match else None


def read_request_filters():
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
    else:
        payload = request.args

    query_text = str(payload.get("query", "")).strip()
    category = payload.get("category") or None
    brand = payload.get("brand") or None

    max_price = payload.get("max_price")
    try:
        budget = float(max_price) if max_price not in (None, "") else None
    except (TypeError, ValueError):
        budget = None

    if budget is None:
        budget = parse_budget_from_text(query_text)

    return {
        "query": query_text,
        "category": category,
        "brand": brand,
        "budget": budget,
    }


def fetch_candidate_products(filters):
    """Fetch database candidates with a relaxed SQL filter, then score them in Python."""
    where_clauses = []
    params = []

    if filters["category"]:
        where_clauses.append("ProductCategory = ?")
        params.append(filters["category"])

    if filters["budget"]:
        # Keep a small above-budget buffer so the scorer can still compare close alternatives.
        where_clauses.append("ProductPrice <= ?")
        params.append(filters["budget"] * 1.15)

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


def calculate_match_score(product, filters):
    score = 8
    reasons = []

    if filters["category"]:
        if product["ProductCategory"] == filters["category"]:
            score += 22
            reasons.append(f"matches category: {filters['category']}")
        else:
            score -= 15

    if filters["brand"]:
        if product["ProductBrand"] == filters["brand"]:
            score += 22
            reasons.append(f"matches brand: {filters['brand']}")
        else:
            score -= 8

    if filters["budget"]:
        price = float(product["ProductPrice"])
        budget = float(filters["budget"])
        if price <= budget:
            price_ratio = price / budget
            ideal_ratio = 0.7
            price_score = round(18 - abs(price_ratio - ideal_ratio) * 24)
            price_score = max(6, min(18, price_score))
            score += price_score
            reasons.append(f"within budget ${budget:.0f}")
        else:
            over_budget_ratio = (price - budget) / budget
            penalty = min(35, round(over_budget_ratio * 40))
            score -= penalty
            reasons.append(f"slightly above budget ${budget:.0f}")

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

    return max(0, min(100, score)), reasons[:4]


def build_leaderboard(filters, limit=5):
    setup_database()
    candidates = fetch_candidate_products(filters)

    if not candidates:
        return []

    leaderboard = []
    for product in candidates:
        score, reasons = calculate_match_score(product, filters)
        leaderboard.append(
            {
                "product_id": int(product["ProductID"]),
                "product_name": f"{product['ProductBrand']} {product['ProductCategory']} #{product['ProductID']}",
                "category": product["ProductCategory"],
                "brand": product["ProductBrand"],
                "price": round(float(product["ProductPrice"]), 2),
                "match_score": score,
                "reason": "; ".join(reasons) or "general product match",
            }
        )

    leaderboard.sort(key=lambda item: (item["match_score"], -item["price"]), reverse=True)
    return leaderboard[:limit]


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

    return jsonify({"status": "success", "data": [dict(row) for row in rows]})


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


if __name__ == "__main__":
    print("Starting backend API server at http://127.0.0.1:5000")
    print("Health check: http://127.0.0.1:5000/api/health")
    app.run(debug=True, port=5000)
