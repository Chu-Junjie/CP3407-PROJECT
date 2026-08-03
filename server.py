"""
Backend API for the Smart Digital Product Recommendation project.

Unified US-05 backend version:
- products table: original 9,000 behaviour/product records.
- product_specs table: 33 educational demonstration specification records.
- feedback table: Helpful / Not Helpful votes saved to SQLite.

The recommendation endpoint intentionally uses INNER JOIN between products and
product_specs so the final UI only receives products that have specification
fields for US-05 comparison. The data is an educational prototype, not a real
market catalogue or real-time price feed.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS


# =============================================================================
# APPLICATION CONFIGURATION
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_CSV_PATH = BASE_DIR / "US-02 Database Setup & Import.csv"
SPECS_CSV_PATH = BASE_DIR / "product_specs.csv"
DB_PATH = BASE_DIR / "digital_products.db"

PRODUCTS_TABLE = "products"
SPECS_TABLE = "product_specs"
FEEDBACK_TABLE = "feedback"

API_VERSION = "2.0.1-unified"
DEFAULT_RECOMMENDATION_LIMIT = 5
MAX_RECOMMENDATION_LIMIT = 5
MAX_QUERY_LENGTH = 1000

SUPPORTED_CATEGORIES = {
    "Laptops",
    "Smartphones",
    "Tablets",
    "Headphones",
    "Smart Watches",
}

CATEGORY_ALIASES = {
    "laptop": "Laptops",
    "laptops": "Laptops",
    "notebook": "Laptops",
    "computer": "Laptops",
    "macbook": "Laptops",
    "phone": "Smartphones",
    "phones": "Smartphones",
    "smartphone": "Smartphones",
    "smartphones": "Smartphones",
    "mobile": "Smartphones",
    "android": "Smartphones",
    "iphone": "Smartphones",
    "tablet": "Tablets",
    "tablets": "Tablets",
    "ipad": "Tablets",
    "headphone": "Headphones",
    "headphones": "Headphones",
    "headset": "Headphones",
    "headsets": "Headphones",
    "earphone": "Headphones",
    "earphones": "Headphones",
    "earbud": "Headphones",
    "earbuds": "Headphones",
    "watch": "Smart Watches",
    "watches": "Smart Watches",
    "smartwatch": "Smart Watches",
    "smartwatches": "Smart Watches",
    "smart watch": "Smart Watches",
    "smart watches": "Smart Watches",
}

GITHUB_PAGES_ORIGIN = "https://chu-junjie.github.io"

PRODUCT_REQUIRED_COLUMNS = {
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

SPECS_REQUIRED_COLUMNS = {
    "ProductID",
    "ProductName",
    "CPU",
    "GPU",
    "RAM",
    "Storage",
    "ScreenSize",
    "BatteryLife",
    "Weight",
    "UseCase",
    "PurchaseURL",
}

app = Flask(__name__)

_default_origins = [
    GITHUB_PAGES_ORIGIN,
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

_extra_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
    if origin.strip()
]

ALLOWED_ORIGINS = sorted(set(_default_origins + _extra_origins))

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ALLOWED_ORIGINS,
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Accept"],
        }
    },
    supports_credentials=False,
    max_age=3600,
)

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


# =============================================================================
# ERROR MODEL
# =============================================================================

@dataclass(slots=True)
class APIError(Exception):
    """Controlled API failure converted into a stable JSON response."""

    message: str
    status_code: int = 400


# =============================================================================
# DATABASE SETUP AND VALIDATION
# =============================================================================

def _environment_flag(name: str, default: bool = False) -> bool:
    """Read a boolean environment variable using common true/false values."""
    raw_value = os.getenv(name)
    if raw_value is None:
        return default
    return raw_value.strip().lower() in {"1", "true", "yes", "on"}


def get_connection() -> sqlite3.Connection:
    """Return a SQLite connection configured for row dictionaries."""
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def _quote_identifier(identifier: str) -> str:
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier):
        raise ValueError(f"Unsafe SQLite identifier: {identifier!r}")
    return f'"{identifier}"'


def _table_exists(connection: sqlite3.Connection, table_name: str) -> bool:
    row = connection.execute(
        """
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table' AND name = ?
        LIMIT 1
        """,
        (table_name,),
    ).fetchone()
    return row is not None


def _table_row_count(connection: sqlite3.Connection, table_name: str) -> int | None:
    if not _table_exists(connection, table_name):
        return None
    return int(
        connection.execute(
            f"SELECT COUNT(*) FROM {_quote_identifier(table_name)}"
        ).fetchone()[0]
    )


def _table_columns(connection: sqlite3.Connection, table_name: str) -> list[str]:
    if not _table_exists(connection, table_name):
        return []
    rows = connection.execute(
        f"PRAGMA table_info({_quote_identifier(table_name)})"
    ).fetchall()
    return [str(row["name"]) for row in rows]


def _import_csv_if_needed(
    connection: sqlite3.Connection,
    table_name: str,
    csv_path: Path,
    required_columns: set[str],
    *,
    force_reload: bool = False,
) -> int:
    """
    Import a CSV when the target table is missing or empty.

    Existing non-empty tables are preserved unless the FORCE_DB_REBUILD
    environment variable is set to 1. This prevents accidental overwrites of
    teammate database work during integration.
    """
    existing_count = _table_row_count(connection, table_name)

    if existing_count is not None and existing_count > 0 and not force_reload:
        existing_columns = set(_table_columns(connection, table_name))
        missing_existing = required_columns.difference(existing_columns)
        if missing_existing:
            missing_text = ", ".join(sorted(missing_existing))
            raise ValueError(
                f"Existing table '{table_name}' is missing required columns: {missing_text}"
            )
        return existing_count

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Missing required dataset '{csv_path.name}'. Place it beside server.py."
        )

    dataframe = pd.read_csv(csv_path)
    missing_columns = required_columns.difference(dataframe.columns)
    if missing_columns:
        missing_text = ", ".join(sorted(missing_columns))
        raise ValueError(f"{csv_path.name} is missing required columns: {missing_text}")

    dataframe.to_sql(table_name, connection, if_exists="replace", index=False)
    connection.commit()
    return int(len(dataframe))


def _create_feedback_table(connection: sqlite3.Connection) -> None:
    connection.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {_quote_identifier(FEEDBACK_TABLE)} (
            feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vote TEXT NOT NULL CHECK (vote IN ('up', 'down')),
            query_text TEXT,
            category TEXT,
            brand TEXT,
            max_price REAL,
            excluded_brands TEXT,
            top_product_id INTEGER,
            recommendation_ids TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.execute(
        f"""
        CREATE INDEX IF NOT EXISTS idx_feedback_created_at
        ON {_quote_identifier(FEEDBACK_TABLE)}(created_at)
        """
    )
    connection.commit()


def _create_indexes(connection: sqlite3.Connection) -> None:
    connection.execute(
        f"""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_products_product_id
        ON {_quote_identifier(PRODUCTS_TABLE)}(ProductID)
        """
    )
    connection.execute(
        f"""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_product_specs_product_id
        ON {_quote_identifier(SPECS_TABLE)}(ProductID)
        """
    )
    connection.execute(
        f"""
        CREATE INDEX IF NOT EXISTS idx_products_category_price
        ON {_quote_identifier(PRODUCTS_TABLE)}(ProductCategory, ProductPrice)
        """
    )
    connection.execute(
        f"""
        CREATE INDEX IF NOT EXISTS idx_products_brand
        ON {_quote_identifier(PRODUCTS_TABLE)}(ProductBrand)
        """
    )
    connection.commit()


def _validate_spec_integrity(connection: sqlite3.Connection) -> None:
    duplicate_specs = connection.execute(
        f"""
        SELECT ProductID, COUNT(*) AS count
        FROM {_quote_identifier(SPECS_TABLE)}
        GROUP BY ProductID
        HAVING COUNT(*) > 1
        LIMIT 1
        """
    ).fetchone()

    if duplicate_specs is not None:
        raise ValueError(
            f"product_specs contains duplicate ProductID: {duplicate_specs['ProductID']}"
        )

    missing_join = connection.execute(
        f"""
        SELECT s.ProductID
        FROM {_quote_identifier(SPECS_TABLE)} s
        LEFT JOIN {_quote_identifier(PRODUCTS_TABLE)} p ON p.ProductID = s.ProductID
        WHERE p.ProductID IS NULL
        LIMIT 1
        """
    ).fetchone()

    if missing_join is not None:
        raise ValueError(
            f"product_specs ProductID {missing_join['ProductID']} does not exist in products"
        )


def setup_database() -> dict[str, int]:
    """Ensure products, product_specs and feedback tables exist."""
    force_reload = _environment_flag("FORCE_DB_REBUILD")

    with get_connection() as connection:
        product_count = _import_csv_if_needed(
            connection,
            PRODUCTS_TABLE,
            PRODUCTS_CSV_PATH,
            PRODUCT_REQUIRED_COLUMNS,
            force_reload=force_reload,
        )
        specs_count = _import_csv_if_needed(
            connection,
            SPECS_TABLE,
            SPECS_CSV_PATH,
            SPECS_REQUIRED_COLUMNS,
            force_reload=force_reload,
        )
        _create_feedback_table(connection)
        _create_indexes(connection)
        _validate_spec_integrity(connection)

        feedback_count = int(
            connection.execute(
                f"SELECT COUNT(*) FROM {_quote_identifier(FEEDBACK_TABLE)}"
            ).fetchone()[0]
        )

    counts = {
        "products": product_count,
        "product_specs": specs_count,
        "feedback": feedback_count,
    }
    logger.info(
        "Database ready: products=%s, product_specs=%s, feedback=%s",
        product_count,
        specs_count,
        feedback_count,
    )
    return counts


def _joined_candidate_count(connection: sqlite3.Connection) -> int:
    return int(
        connection.execute(
            f"""
            SELECT COUNT(*)
            FROM {_quote_identifier(PRODUCTS_TABLE)} p
            INNER JOIN {_quote_identifier(SPECS_TABLE)} s ON p.ProductID = s.ProductID
            """
        ).fetchone()[0]
    )


# =============================================================================
# REQUEST PARSING
# =============================================================================

def _normalise_optional_text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _parse_positive_float(value: Any, field_name: str) -> float | None:
    if value in (None, ""):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise APIError(f"'{field_name}' must be a valid number.", 400) from exc
    if number <= 0:
        raise APIError(f"'{field_name}' must be greater than zero.", 400)
    return number


def _first_provided(*values: Any) -> Any:
    """Return the first value that is not None and not an empty string."""
    for value in values:
        if value not in (None, ""):
            return value
    return None


def _normalise_category(value: Any) -> str | None:
    """Normalise common category names and reject unsupported categories."""
    text = _normalise_optional_text(value)
    if text is None:
        return None

    category = CATEGORY_ALIASES.get(text.lower(), text)
    if category not in SUPPORTED_CATEGORIES:
        allowed = ", ".join(sorted(SUPPORTED_CATEGORIES))
        raise APIError(
            f"Unsupported category '{text}'. Allowed values: {allowed}.",
            400,
        )
    return category


def parse_budget_from_text(text: str | None) -> float | None:
    if not text:
        return None

    normalised = str(text).lower().replace(",", "")
    patterns = [
        (
            r"(?:under|below|less\s+than|budget(?:\s+(?:of|is))?|"
            r"around|up\s+to|maximum|max|limit(?:\s+is)?)"
            r"\s*\$?\s*(\d+(?:\.\d+)?)"
        ),
        r"\$\s*(\d+(?:\.\d+)?)",
    ]

    for pattern in patterns:
        match = re.search(pattern, normalised)
        if match:
            return float(match.group(1))

    return None


def parse_use_case_keywords(text: str | None) -> list[str]:
    if not text:
        return []

    lowered = str(text).lower()
    keyword_map = {
        "gaming": ["gaming", "game", "play", "fps"],
        "study": ["study", "student", "school", "university", "homework"],
        "office": ["office", "work", "business", "productivity"],
        "portable": ["portable", "light", "travel", "thin"],
        "battery": ["battery", "long lasting", "long-lasting", "durable"],
        "creative": ["creative", "video editing", "design", "photoshop"],
        "3d": ["3d", "modelling", "modeling", "render"],
        "camera": ["camera", "photo", "video"],
        "budget": ["cheap", "budget", "affordable", "value"],
    }

    return [
        label
        for label, phrases in keyword_map.items()
        if any(phrase in lowered for phrase in phrases)
    ]


def infer_category_from_text(text: str | None) -> str | None:
    if not text:
        return None

    lowered = str(text).lower()
    ordered_terms = sorted(
        CATEGORY_ALIASES,
        key=len,
        reverse=True,
    )

    for term in ordered_terms:
        if re.search(rf"\b{re.escape(term)}\b", lowered):
            return CATEGORY_ALIASES[term]
    return None


def _known_brands_from_specs() -> list[str]:
    setup_database()
    with get_connection() as connection:
        rows = connection.execute(
            f"""
            SELECT DISTINCT p.ProductBrand AS brand
            FROM {_quote_identifier(PRODUCTS_TABLE)} p
            INNER JOIN {_quote_identifier(SPECS_TABLE)} s ON p.ProductID = s.ProductID
            WHERE p.ProductBrand IS NOT NULL
            ORDER BY p.ProductBrand
            """
        ).fetchall()
    return [str(row["brand"]) for row in rows]


def parse_exclusions(text: str | None, explicit: Any = None) -> list[str]:
    exclusions: list[str] = []

    if text:
        matches = re.findall(
            r"\b(?:no|exclude|without|avoid)\s+([a-zA-Z0-9_\- ]+?)\b(?=\s*(?:,|and|or|$))",
            str(text),
            flags=re.IGNORECASE,
        )
        for match in matches:
            value = match.strip().lower()
            if value:
                exclusions.append(value)

        # Preserve the simple one-word behaviour for phrases like "no Apple".
        simple_matches = re.findall(
            r"\b(?:no|exclude|without|avoid)\s+([a-zA-Z0-9_-]+)\b",
            str(text),
            flags=re.IGNORECASE,
        )
        exclusions.extend(match.strip().lower() for match in simple_matches if match.strip())

    if isinstance(explicit, str):
        exclusions.extend(item.strip().lower() for item in explicit.split(",") if item.strip())
    elif isinstance(explicit, list):
        exclusions.extend(str(item).strip().lower() for item in explicit if str(item).strip())

    return list(dict.fromkeys(exclusions))


def infer_brand_from_text(text: str | None, exclusions: Iterable[str]) -> str | None:
    if not text:
        return None

    lowered = str(text).lower()
    excluded_set = {str(item).lower() for item in exclusions}

    for brand in _known_brands_from_specs():
        if brand.lower() in lowered and brand.lower() not in excluded_set:
            return brand
    return None


def _read_request_payload() -> dict[str, Any]:
    if request.method == "POST":
        payload = request.get_json(silent=True)
        if payload is None:
            if request.data:
                raise APIError("Request body must contain valid JSON.", 400)
            return {}
        if not isinstance(payload, dict):
            raise APIError("JSON request body must be an object.", 400)
        return payload
    return request.args.to_dict(flat=True)


def read_request_filters() -> dict[str, Any]:
    payload = _read_request_payload()

    query_text = str(payload.get("query") or payload.get("intent") or "").strip()
    if len(query_text) > MAX_QUERY_LENGTH:
        raise APIError(f"'query' must not exceed {MAX_QUERY_LENGTH} characters.", 400)

    category = _normalise_category(payload.get("category")) or infer_category_from_text(query_text)

    explicit_exclusions = (
        payload.get("excluded_brands")
        if payload.get("excluded_brands") not in (None, "")
        else payload.get("exclusions")
    )
    exclusions = parse_exclusions(query_text, explicit_exclusions)

    brand = _normalise_optional_text(payload.get("brand")) or infer_brand_from_text(query_text, exclusions)

    explicit_budget = (
        payload.get("max_price")
        if payload.get("max_price") not in (None, "")
        else payload.get("budget")
    )
    max_price = _parse_positive_float(explicit_budget, "max_price")
    if max_price is None:
        max_price = parse_budget_from_text(query_text)

    requested_limit = payload.get("limit", DEFAULT_RECOMMENDATION_LIMIT)
    try:
        limit = int(requested_limit)
    except (TypeError, ValueError) as exc:
        raise APIError("'limit' must be an integer.", 400) from exc
    limit = max(1, min(MAX_RECOMMENDATION_LIMIT, limit))

    return {
        "query": query_text,
        "category": category,
        "brand": brand,
        "budget": max_price,
        "max_price": max_price,
        "exclusions": exclusions,
        "excluded_brands": exclusions,
        "use_cases": parse_use_case_keywords(query_text),
        "limit": limit,
    }


# =============================================================================
# PRODUCT DATA ACCESS AND RANKING
# =============================================================================

def _base_join_sql() -> str:
    return f"""
        SELECT
            p.ProductID,
            p.ProductCategory,
            p.ProductBrand,
            p.ProductPrice,
            p.CustomerAge,
            p.CustomerGender,
            p.PurchaseFrequency,
            p.CustomerSatisfaction,
            p.PurchaseIntent,
            s.ProductName,
            s.CPU,
            s.GPU,
            s.RAM,
            s.Storage,
            s.ScreenSize,
            s.BatteryLife,
            s.Weight,
            s.UseCase,
            s.PurchaseURL
        FROM {_quote_identifier(PRODUCTS_TABLE)} p
        INNER JOIN {_quote_identifier(SPECS_TABLE)} s ON p.ProductID = s.ProductID
    """


def fetch_candidate_products(
    filters: dict[str, Any],
    *,
    strict_brand: bool = False,
) -> list[dict[str, Any]]:
    setup_database()

    where_clauses: list[str] = []
    params: list[Any] = []

    if filters.get("category"):
        where_clauses.append("LOWER(TRIM(p.ProductCategory)) = LOWER(TRIM(?))")
        params.append(str(filters["category"]))

    if filters.get("budget") is not None:
        where_clauses.append("CAST(p.ProductPrice AS REAL) <= ?")
        params.append(float(filters["budget"]))

    if strict_brand and filters.get("brand"):
        where_clauses.append(
            "LOWER(TRIM(p.ProductBrand)) = LOWER(TRIM(?))"
        )
        params.append(str(filters["brand"]))

    for exclusion in filters.get("exclusions", []):
        where_clauses.append("LOWER(TRIM(p.ProductBrand)) != LOWER(TRIM(?))")
        params.append(str(exclusion))

    where_sql = f"WHERE {' AND '.join(where_clauses)}" if where_clauses else ""

    sql = f"""
        {_base_join_sql()}
        {where_sql}
        ORDER BY CAST(p.ProductPrice AS REAL) ASC
    """

    with get_connection() as connection:
        rows = connection.execute(sql, params).fetchall()

    return [dict(row) for row in rows]


def _optional_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def calculate_match_score(product: dict[str, Any], filters: dict[str, Any]) -> tuple[int, list[str]]:
    score = 10
    reasons: list[str] = []

    category = filters.get("category")
    if category:
        if str(product["ProductCategory"]).strip().lower() == str(category).strip().lower():
            score += 22
            reasons.append(f"matches category: {category}")
        else:
            score -= 15

    brand = filters.get("brand")
    if brand:
        if str(product["ProductBrand"]).strip().lower() == str(brand).strip().lower():
            score += 18
            reasons.append(f"matches preferred brand: {brand}")
        else:
            score -= 5

    budget = filters.get("budget")
    price = float(product["ProductPrice"])
    if budget is not None:
        budget_value = float(budget)
        if budget_value > 0 and price <= budget_value:
            price_ratio = price / budget_value
            price_score = round(18 - abs(price_ratio - 0.70) * 24)
            score += max(6, min(18, price_score))
            reasons.append(f"within budget ${budget_value:.0f}")

    use_case_text = str(product.get("UseCase") or "").lower()
    matched_use_cases = [
        use_case for use_case in filters.get("use_cases", []) if use_case in use_case_text
    ]
    if matched_use_cases:
        score += min(14, len(matched_use_cases) * 5)
        reasons.append("fits " + ", ".join(matched_use_cases))

    satisfaction = _optional_float(product.get("CustomerSatisfaction"))
    if satisfaction is not None:
        score += round(max(0.0, min(5.0, satisfaction)) / 5.0 * 10)
        if satisfaction >= 4:
            reasons.append("high customer satisfaction")

    purchase_frequency = _optional_float(product.get("PurchaseFrequency"))
    if purchase_frequency is not None:
        if purchase_frequency >= 7:
            score += 5
            reasons.append("strong purchase frequency")
        elif purchase_frequency >= 4:
            score += 2

    purchase_intent = _optional_float(product.get("PurchaseIntent"))
    if purchase_intent is not None and purchase_intent >= 1:
        score += 4
        reasons.append("positive purchase intent")

    if product.get("ProductName"):
        score += 3
        reasons.append("specification data available")

    return max(0, min(100, int(round(score)))), reasons[:5]


def product_payload(
    product: dict[str, Any],
    *,
    score: int | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    product_name = (
        product.get("ProductName")
        or f"{product['ProductBrand']} {product['ProductCategory']} #{product['ProductID']}"
    )

    specs = {
        "cpu": product.get("CPU"),
        "gpu": product.get("GPU"),
        "ram": product.get("RAM"),
        "storage": product.get("Storage"),
        "screen_size": product.get("ScreenSize"),
        "battery_life": product.get("BatteryLife"),
        "weight": product.get("Weight"),
        "use_case": product.get("UseCase"),
    }

    payload: dict[str, Any] = {
        "product_id": int(product["ProductID"]),
        "product_name": product_name,
        "name": product_name,
        "category": product["ProductCategory"],
        "brand": product["ProductBrand"],
        "price": round(float(product["ProductPrice"]), 2),
        "price_type": "prototype",
        "price_note": (
            "Used for course-project filtering and comparison; "
            "not guaranteed to be a current Singapore retail price."
        ),
        "specs": specs,
        "cpu": specs["cpu"],
        "gpu": specs["gpu"],
        "ram": specs["ram"],
        "storage": specs["storage"],
        "screen_size": specs["screen_size"],
        "battery_life": specs["battery_life"],
        "weight": specs["weight"],
        "use_case": specs["use_case"],
        "purchase_url": product.get("PurchaseURL") or "",
    }

    if score is not None:
        payload["match_score"] = score
        payload["score"] = score
    if reason is not None:
        payload["reason"] = reason

    return payload


def build_leaderboard(filters: dict[str, Any], limit: int = DEFAULT_RECOMMENDATION_LIMIT) -> list[dict[str, Any]]:
    candidates = fetch_candidate_products(filters)
    leaderboard: list[dict[str, Any]] = []

    for product in candidates:
        score, reasons = calculate_match_score(product, filters)
        item = product_payload(
            product,
            score=score,
            reason="; ".join(reasons) or "general product match",
        )
        leaderboard.append(item)

    leaderboard.sort(key=lambda item: (-int(item["match_score"]), float(item["price"])))
    return leaderboard[: max(0, min(MAX_RECOMMENDATION_LIMIT, int(limit)))]


def find_budget_alternative(
    filters: dict[str, Any],
    leaderboard: Sequence[dict[str, Any]],
) -> dict[str, Any] | None:
    if not leaderboard:
        return None

    reference = leaderboard[0]
    category = filters.get("category") or reference.get("category")
    reference_price = float(reference["price"])
    excluded_ids = {int(item["product_id"]) for item in leaderboard}

    alt_filters = {
        **filters,
        "category": category,
        # Do not apply the user's original budget as the only criterion here;
        # the alternative must simply be cheaper than the current top result.
        "budget": None,
    }

    candidates = fetch_candidate_products(alt_filters)
    cheaper_candidates = [
        product
        for product in candidates
        if int(product["ProductID"]) not in excluded_ids
        and float(product["ProductPrice"]) < reference_price
    ]

    if not cheaper_candidates:
        return None

    cheaper_candidates.sort(key=lambda item: float(item["ProductPrice"]))
    product = cheaper_candidates[0]
    score, reasons = calculate_match_score(product, filters)
    reason = "; ".join(reasons) or "cheaper product in the same category"
    payload = product_payload(product, score=score, reason=reason)
    payload["alternative_reason"] = "Cheaper product in the same category."
    return payload


def _parse_compare_ids() -> list[int]:
    payload = _read_request_payload() if request.method == "POST" else {}
    raw_ids = payload.get("product_ids") or payload.get("ids") or request.args.get("ids", "")

    if isinstance(raw_ids, list):
        candidates = raw_ids
    else:
        candidates = str(raw_ids).split(",")

    product_ids: list[int] = []
    for candidate in candidates:
        candidate_text = str(candidate).strip()
        if not candidate_text:
            continue
        try:
            product_id = int(candidate_text)
        except ValueError as exc:
            raise APIError(
                f"Invalid product ID: {candidate_text}. Product IDs must be integers.",
                400,
            ) from exc
        if product_id <= 0:
            raise APIError("Product IDs must be greater than zero.", 400)
        product_ids.append(product_id)

    if len(product_ids) not in (2, 3):
        raise APIError("Provide exactly 2 or 3 product IDs.", 400)
    if len(set(product_ids)) != len(product_ids):
        raise APIError("Product IDs must be unique.", 400)
    return product_ids


def fetch_products_for_compare(product_ids: Sequence[int]) -> list[dict[str, Any]]:
    setup_database()
    placeholders = ",".join("?" for _ in product_ids)
    sql = f"""
        {_base_join_sql()}
        WHERE p.ProductID IN ({placeholders})
    """

    with get_connection() as connection:
        rows = connection.execute(sql, list(product_ids)).fetchall()

    products_by_id = {int(row["ProductID"]): dict(row) for row in rows}
    missing_ids = [product_id for product_id in product_ids if product_id not in products_by_id]

    if missing_ids:
        raise APIError(
            "One or more products do not exist or have no specification data.",
            400,
        )

    return [products_by_id[product_id] for product_id in product_ids]


# =============================================================================
# FEEDBACK
# =============================================================================

def _normalise_vote(value: Any) -> str:
    vote_text = str(value or "").strip().lower()
    up_values = {"up", "helpful", "positive", "yes", "thumbs_up", "like"}
    down_values = {"down", "not_helpful", "negative", "no", "thumbs_down", "dislike"}

    if vote_text in up_values:
        return "up"
    if vote_text in down_values:
        return "down"
    raise APIError("'vote' must be either 'up' or 'down'.", 400)


def save_feedback(payload: dict[str, Any]) -> int:
    setup_database()

    vote = _normalise_vote(payload.get("vote"))
    filters = payload.get("filters") if isinstance(payload.get("filters"), dict) else {}

    query_text = str(payload.get("query") or filters.get("query") or "").strip() or None
    category = _normalise_optional_text(payload.get("category") or filters.get("category"))
    brand = _normalise_optional_text(payload.get("brand") or filters.get("brand"))
    max_price = _parse_positive_float(
        _first_provided(
            payload.get("max_price"),
            payload.get("budget"),
            filters.get("max_price"),
            filters.get("budget"),
        ),
        "max_price",
    )

    excluded_brands = (
        payload.get("excluded_brands")
        or payload.get("exclusions")
        or filters.get("excluded_brands")
        or filters.get("exclusions")
        or []
    )
    if not isinstance(excluded_brands, list):
        excluded_brands = [str(excluded_brands)] if excluded_brands else []

    recommendation_ids = payload.get("recommendation_ids") or []
    if not isinstance(recommendation_ids, list):
        recommendation_ids = []

    top_product_id = _first_provided(payload.get("top_product_id"), payload.get("product_id"))
    if top_product_id in (None, ""):
        top_product_id_value = None
    else:
        try:
            top_product_id_value = int(top_product_id)
        except (TypeError, ValueError) as exc:
            raise APIError("'top_product_id' must be an integer when supplied.", 400) from exc

    with get_connection() as connection:
        cursor = connection.execute(
            f"""
            INSERT INTO {_quote_identifier(FEEDBACK_TABLE)}
                (vote, query_text, category, brand, max_price, excluded_brands,
                 top_product_id, recommendation_ids)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                vote,
                query_text,
                category,
                brand,
                max_price,
                json.dumps(excluded_brands),
                top_product_id_value,
                json.dumps(recommendation_ids),
            ),
        )
        connection.commit()
        return int(cursor.lastrowid)


# =============================================================================
# API ROUTES
# =============================================================================

@app.after_request
def add_api_response_headers(response):
    if request.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.route("/", methods=["GET"])
def api_home():
    """Return basic information about the deployed API service."""
    return jsonify(
        {
            "status": "success",
            "message": "Smart Digital Product Recommendation API is running.",
            "api_version": API_VERSION,
            "endpoints": {
                "health": "/api/health",
                "products": "/api/products",
                "recommend": "/api/recommend",
                "compare": "/api/compare",
                "feedback": "/api/feedback",
            },
        }
    )


@app.route("/api/health", methods=["GET"])
def health_check():
    counts = setup_database()
    with get_connection() as connection:
        joined_count = _joined_candidate_count(connection)
        products_columns = _table_columns(connection, PRODUCTS_TABLE)
        specs_columns = _table_columns(connection, SPECS_TABLE)

    return jsonify(
        {
            "status": "success",
            "api_version": API_VERSION,
            "database": DB_PATH.name,
            "tables": {
                "products": {
                    "name": PRODUCTS_TABLE,
                    "records": counts["products"],
                    "columns": products_columns,
                },
                "product_specs": {
                    "name": SPECS_TABLE,
                    "records": counts["product_specs"],
                    "columns": specs_columns,
                },
                "feedback": {
                    "name": FEEDBACK_TABLE,
                    "records": counts["feedback"],
                },
            },
            "joined_recommendation_candidates": joined_count,
            "notes": "Recommendations use INNER JOIN, so only products with specification data are returned.",
        }
    )


@app.route("/api/products", methods=["GET"])
def products():
    setup_database()
    try:
        requested_limit = int(request.args.get("limit", 10))
    except ValueError as exc:
        raise APIError("'limit' must be an integer.", 400) from exc
    limit = max(1, min(20, requested_limit))

    filters = {
        "query": "",
        "category": _normalise_category(request.args.get("category")),
        "brand": _normalise_optional_text(request.args.get("brand")),
        "budget": None,
        "exclusions": [],
        "use_cases": [],
    }

    rows = fetch_candidate_products(filters, strict_brand=True)[:limit]
    data = [product_payload(row) for row in rows]
    return jsonify({"status": "success", "count": len(data), "data": data})


@app.route("/api/recommend", methods=["GET", "POST"])
def recommend():
    filters = read_request_filters()
    limit = int(filters.get("limit", DEFAULT_RECOMMENDATION_LIMIT))

    leaderboard = build_leaderboard(filters, limit=limit)
    budget_alternative = find_budget_alternative(filters, leaderboard)

    message = (
        f"Returned {len(leaderboard)} recommendation(s) from products with specification data."
        if leaderboard
        else "No matching products with specification data were found."
    )

    response_filters = dict(filters)
    response_filters.pop("limit", None)

    return jsonify(
        {
            "status": "success",
            "message": message,
            "filters": response_filters,
            "count": len(leaderboard),
            "data": leaderboard,
            "budget_alternative": budget_alternative,
        }
    )


@app.route("/api/compare", methods=["GET", "POST"])
def compare_products():
    product_ids = _parse_compare_ids()
    products = fetch_products_for_compare(product_ids)
    data = [product_payload(product) for product in products]

    return jsonify(
        {
            "status": "success",
            "message": "Comparison data returned for selected products.",
            "requested_ids": product_ids,
            "count": len(data),
            "data": data,
        }
    )


@app.route("/api/feedback", methods=["POST"])
def feedback():
    payload = _read_request_payload()
    feedback_id = save_feedback(payload)

    return jsonify(
        {
            "status": "success",
            "message": "Feedback saved.",
            "feedback_id": feedback_id,
        }
    ), 201


# =============================================================================
# ERROR HANDLERS
# =============================================================================

@app.errorhandler(APIError)
def handle_api_error(error: APIError):
    return jsonify({"status": "error", "message": error.message}), error.status_code


@app.errorhandler(FileNotFoundError)
def handle_missing_file(error: FileNotFoundError):
    logger.error("Required data file missing: %s", error)
    return jsonify({"status": "error", "message": str(error)}), 500


@app.errorhandler(ValueError)
def handle_invalid_data(error: ValueError):
    logger.error("Invalid application data: %s", error)
    return jsonify({"status": "error", "message": str(error)}), 500


@app.errorhandler(sqlite3.Error)
def handle_database_error(error: sqlite3.Error):
    logger.exception("Database operation failed: %s", error)
    return jsonify(
        {
            "status": "error",
            "message": "A database operation failed. Please try again later.",
        }
    ), 500


@app.errorhandler(404)
def handle_not_found(_error):
    return jsonify({"status": "error", "message": "API endpoint not found."}), 404


@app.errorhandler(405)
def handle_method_not_allowed(_error):
    return jsonify(
        {"status": "error", "message": "HTTP method not allowed for this endpoint."}
    ), 405


@app.errorhandler(Exception)
def handle_unexpected_error(error: Exception):
    logger.exception("Unhandled backend exception: %s", error)
    return jsonify(
        {"status": "error", "message": "An unexpected server error occurred."}
    ), 500


# =============================================================================
# LOCAL ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))
    debug = _environment_flag("FLASK_DEBUG")

    logger.info("Starting recommendation API on http://%s:%s", host, port)
    logger.info("Allowed CORS origins: %s", ", ".join(ALLOWED_ORIGINS))
    logger.info("Health endpoint: http://%s:%s/api/health", host, port)

    app.run(host=host, port=port, debug=debug)
