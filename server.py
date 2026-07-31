"""
Backend API for the Smart Digital Product Recommendation project.

This module provides a small REST API that separates the static GitHub Pages
frontend from the recommendation logic and product database. The design keeps
the API contract stable while allowing the database schema to evolve during
iterative development.

Frontend origin:
    https://chu-junjie.github.io/CP3407-PROJECT/

Primary endpoint:
    POST /api/recommend

Example request:
    {
        "query": "I need a laptop under $1500, no Apple"
    }

Example response:
    {
        "status": "success",
        "filters": {
            "query": "I need a laptop under $1500, no Apple",
            "category": "Laptops",
            "brand": null,
            "budget": 1500.0,
            "exclusions": ["apple"]
        },
        "data": [...]
    }
"""

from __future__ import annotations

import logging
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS


# =============================================================================
# APPLICATION CONFIGURATION
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "US-02 Database Setup & Import.csv"
DB_PATH = BASE_DIR / "digital_products.db"
TABLE_NAME = "products"

API_VERSION = "1.0.0"
DEFAULT_RECOMMENDATION_LIMIT = 5
MAX_RECOMMENDATION_LIMIT = 5
MAX_QUERY_LENGTH = 1000

GITHUB_PAGES_ORIGIN = "https://chu-junjie.github.io"

app = Flask(__name__)

# Restrict cross-origin access to the deployed GitHub Pages site and common
# local development origins. Additional origins can be supplied through the
# CORS_ALLOWED_ORIGINS environment variable as a comma-separated list.
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
# API ERROR MODEL
# =============================================================================

@dataclass(slots=True)
class APIError(Exception):
    """
    Represent a controlled API failure.

    Controlled exceptions allow the application to return consistent JSON
    responses for invalid client input without exposing implementation details.
    """

    message: str
    status_code: int = 400


# =============================================================================
# DATABASE SCHEMA COMPATIBILITY
# =============================================================================

# Canonical API fields are mapped to both the original Week 7 dataset names
# and likely snake_case names. This supports the current database while reducing
# coupling between the API layer and a future database redesign.
FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "product_id": ("product_id", "ProductID", "id"),
    "product_name": ("product_name", "ProductName", "name"),
    "category": ("category", "product_category", "ProductCategory"),
    "brand": ("brand", "product_brand", "ProductBrand"),
    "price": ("price", "product_price", "ProductPrice"),
    "customer_age": ("customer_age", "CustomerAge"),
    "customer_gender": ("customer_gender", "CustomerGender"),
    "purchase_frequency": ("purchase_frequency", "PurchaseFrequency"),
    "customer_satisfaction": ("customer_satisfaction", "CustomerSatisfaction"),
    "purchase_intent": ("purchase_intent", "PurchaseIntent"),
    "cpu": ("cpu", "CPU"),
    "gpu": ("gpu", "GPU"),
    "ram": ("ram", "ram_gb", "RAM", "RAM_GB"),
    "storage": ("storage", "storage_gb", "Storage", "Storage_GB"),
    "screen": ("screen", "screen_size", "Screen", "ScreenSize"),
    "battery": ("battery", "battery_life", "Battery", "BatteryLife"),
    "weight": ("weight", "weight_kg", "Weight", "WeightKG"),
    "purchase_url": ("purchase_url", "PurchaseURL", "url", "URL"),
}

CORE_FIELDS = ("product_id", "category", "brand", "price")

INITIAL_DATASET_COLUMNS = {
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


def get_connection() -> sqlite3.Connection:
    """
    Return a SQLite connection configured for dictionary-like row access.

    A new connection is created for each operation. This is appropriate for the
    current lightweight Flask application and avoids sharing a SQLite connection
    across concurrent requests.
    """
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    return connection


def _table_exists(connection: sqlite3.Connection) -> bool:
    """Return True when the configured product table exists."""
    result = connection.execute(
        """
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table' AND name = ?
        LIMIT 1
        """,
        (TABLE_NAME,),
    ).fetchone()

    return result is not None


def setup_database() -> int:
    """
    Ensure that a usable product table exists and return its record count.

    Existing non-empty databases are preserved. The original CSV file is used
    only as a bootstrap source when the table does not yet exist or is empty.
    This behaviour avoids overwriting a teammate's later database work.
    """
    with get_connection() as connection:
        if _table_exists(connection):
            row_count = connection.execute(
                f'SELECT COUNT(*) FROM "{TABLE_NAME}"'
            ).fetchone()[0]

            if row_count > 0:
                _validate_active_schema(connection)
                return int(row_count)

    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"Product database is empty and bootstrap dataset "
            f"'{CSV_PATH.name}' could not be found."
        )

    dataframe = pd.read_csv(CSV_PATH)

    missing_columns = INITIAL_DATASET_COLUMNS.difference(dataframe.columns)
    if missing_columns:
        missing_text = ", ".join(sorted(missing_columns))
        raise ValueError(
            f"Bootstrap dataset is missing required columns: {missing_text}"
        )

    with get_connection() as connection:
        dataframe.to_sql(
            TABLE_NAME,
            connection,
            if_exists="replace",
            index=False,
        )
        connection.commit()
        _validate_active_schema(connection)

    logger.info("Bootstrapped product database with %s records.", len(dataframe))
    return int(len(dataframe))


def _get_table_columns(connection: sqlite3.Connection) -> list[str]:
    """Return the column names currently present in the product table."""
    rows = connection.execute(
        f'PRAGMA table_info("{TABLE_NAME}")'
    ).fetchall()

    return [str(row["name"]) for row in rows]


def _resolve_schema(columns: Iterable[str]) -> dict[str, str]:
    """
    Map canonical application fields to actual database column names.

    The API layer uses canonical names while this adapter isolates differences
    between the original dataset naming convention and a future schema.
    """
    available = set(columns)
    resolved: dict[str, str] = {}

    for canonical_name, aliases in FIELD_ALIASES.items():
        actual_name = next(
            (alias for alias in aliases if alias in available),
            None,
        )

        if actual_name is not None:
            resolved[canonical_name] = actual_name

    return resolved


def _validate_active_schema(connection: sqlite3.Connection) -> None:
    """
    Confirm that the active table contains the minimum data required to rank
    products. Optional specification and behavioural columns may be absent.
    """
    schema = _resolve_schema(_get_table_columns(connection))
    missing = [field for field in CORE_FIELDS if field not in schema]

    if missing:
        raise ValueError(
            "Product database is missing required logical fields: "
            + ", ".join(missing)
        )


def _active_schema() -> dict[str, str]:
    """Return the canonical-to-physical mapping for the active product table."""
    setup_database()

    with get_connection() as connection:
        return _resolve_schema(_get_table_columns(connection))


def _quote_identifier(identifier: str) -> str:
    """
    Quote a verified SQLite identifier.

    Identifiers are obtained from schema introspection rather than user input.
    The defensive pattern check prevents accidental unsafe SQL construction.
    """
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier):
        raise ValueError(f"Unsafe database identifier: {identifier!r}")

    return f'"{identifier}"'


# =============================================================================
# NATURAL-LANGUAGE AND REQUEST PROCESSING
# =============================================================================

def parse_budget_from_text(text: str | None) -> float | None:
    """
    Extract a maximum budget from common natural-language expressions.

    Supported examples include:
        "$1,500"
        "under 1500"
        "below $900"
        "budget 1200"
        "up to 2000"
    """
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


def _normalise_optional_text(value: Any) -> str | None:
    """Convert an optional request value into stripped text or None."""
    if value is None:
        return None

    text = str(value).strip()
    return text or None


def _normalise_phrase(value: str) -> str:
    """Normalise free text for case-insensitive phrase comparison."""
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _singularise_word(word: str) -> str:
    """
    Apply a lightweight singularisation heuristic for category matching.

    This is intentionally conservative and is not intended to replace a full
    natural-language processing library.
    """
    if len(word) <= 3:
        return word

    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"

    if word.endswith(("ches", "shes", "xes", "zes")):
        return word[:-2]

    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]

    return word


def _normalised_variants(value: str) -> set[str]:
    """Return plural and lightweight singular phrase variants."""
    normalised = _normalise_phrase(value)
    if not normalised:
        return set()

    singular = " ".join(
        _singularise_word(word)
        for word in normalised.split()
    )

    return {normalised, singular}


def _known_dimension_values(field: str) -> list[str]:
    """Read distinct category or brand values from the active database."""
    schema = _active_schema()

    if field not in schema:
        return []

    column = _quote_identifier(schema[field])

    with get_connection() as connection:
        rows = connection.execute(
            f"""
            SELECT DISTINCT {column} AS value
            FROM "{TABLE_NAME}"
            WHERE {column} IS NOT NULL
              AND TRIM(CAST({column} AS TEXT)) != ''
            """
        ).fetchall()

    return [str(row["value"]).strip() for row in rows]


def _infer_known_value(text: str, values: Iterable[str]) -> str | None:
    """
    Infer a category or brand by matching known database values in the query.

    Matching against the database taxonomy makes the parser data-driven and
    avoids maintaining a separate hard-coded list of product brands.
    """
    query = f" {_normalise_phrase(text)} "

    if not query.strip():
        return None

    # Prefer longer values first to avoid a short brand/category name masking
    # a more specific multi-word value.
    ordered_values = sorted(
        (value for value in values if value),
        key=lambda item: len(_normalise_phrase(item)),
        reverse=True,
    )

    for value in ordered_values:
        for variant in _normalised_variants(value):
            if variant and f" {variant} " in query:
                return value

    return None


def parse_exclusions(
    text: str | None,
    known_brands: Iterable[str] | None = None,
) -> list[str]:
    """
    Extract excluded brands or keywords from a natural-language query.

    Examples:
        "no Apple" -> ["apple"]
        "exclude Sony" -> ["sony"]
        "without Samsung" -> ["samsung"]

    When database brand names are available, the function also recognises
    multi-word brands following exclusion phrases.
    """
    if not text:
        return []

    raw_text = str(text)
    exclusions: list[str] = []

    # Preserve compatibility with the original simple parser.
    simple_matches = re.findall(
        r"\b(?:no|exclude|without|avoid)\s+([a-zA-Z0-9_-]+)\b",
        raw_text,
        flags=re.IGNORECASE,
    )

    exclusions.extend(
        match.strip().lower()
        for match in simple_matches
        if match.strip()
    )

    if known_brands:
        lower_text = raw_text.lower()

        for brand in known_brands:
            brand_text = str(brand).strip()
            if not brand_text:
                continue

            escaped_brand = re.escape(brand_text.lower())

            patterns = [
                rf"\b(?:no|exclude|without|avoid)\s+{escaped_brand}\b",
                rf"\b(?:no|exclude|without|avoid)\s+products?\s+from\s+{escaped_brand}\b",
            ]

            if any(re.search(pattern, lower_text) for pattern in patterns):
                exclusions.append(brand_text.lower())

    # Preserve order while removing duplicates.
    return list(dict.fromkeys(exclusions))


def _parse_optional_positive_float(
    value: Any,
    field_name: str,
) -> float | None:
    """Parse a positive numeric request field or raise a controlled 400 error."""
    if value in (None, ""):
        return None

    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise APIError(
            f"'{field_name}' must be a valid number.",
            400,
        ) from exc

    if number < 0:
        raise APIError(
            f"'{field_name}' cannot be negative.",
            400,
        )

    return number


def _read_request_payload() -> dict[str, Any]:
    """
    Return request parameters as a standard dictionary.

    POST requests use JSON. GET support is retained for backwards compatibility
    and lightweight manual testing.
    """
    if request.method == "POST":
        payload = request.get_json(silent=True)

        if payload is None:
            return {}

        if not isinstance(payload, dict):
            raise APIError("JSON request body must be an object.", 400)

        return payload

    return request.args.to_dict(flat=True)


def read_request_filters() -> dict[str, Any]:
    """
    Convert request data into validated recommendation filters.

    Direct structured fields take precedence. Missing category and preferred
    brand values are inferred from the natural-language query using values
    already present in the product database.
    """
    payload = _read_request_payload()

    # "intent" is retained for compatibility with earlier project tests.
    query_text = str(
        payload.get("query")
        or payload.get("intent")
        or ""
    ).strip()

    if len(query_text) > MAX_QUERY_LENGTH:
        raise APIError(
            f"'query' must not exceed {MAX_QUERY_LENGTH} characters.",
            400,
        )

    known_categories = _known_dimension_values("category")
    known_brands = _known_dimension_values("brand")

    category = _normalise_optional_text(payload.get("category"))
    brand = _normalise_optional_text(payload.get("brand"))

    if category is None and query_text:
        category = _infer_known_value(query_text, known_categories)

    explicit_exclusions = payload.get("exclusions")
    exclusions = parse_exclusions(query_text, known_brands)

    if isinstance(explicit_exclusions, list):
        exclusions.extend(
            str(item).strip().lower()
            for item in explicit_exclusions
            if str(item).strip()
        )

    exclusions = list(dict.fromkeys(exclusions))

    if brand is None and query_text:
        inferred_brand = _infer_known_value(query_text, known_brands)

        if (
            inferred_brand is not None
            and inferred_brand.lower() not in exclusions
        ):
            brand = inferred_brand

    explicit_budget = (
        payload.get("max_price")
        if payload.get("max_price") not in (None, "")
        else payload.get("budget")
    )

    budget = _parse_optional_positive_float(
        explicit_budget,
        "max_price",
    )

    if budget is None:
        budget = parse_budget_from_text(query_text)

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
        "budget": budget,
        "exclusions": exclusions,
        "limit": limit,
    }


# =============================================================================
# RECOMMENDATION DATA ACCESS
# =============================================================================

def fetch_candidate_products(
    filters: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Return products satisfying hard constraints.

    Category, maximum budget, and explicit brand exclusions are treated as hard
    filters. Preferred brand is treated as a ranking signal rather than a hard
    constraint so that useful alternatives can still be recommended.
    """
    setup_database()
    schema = _active_schema()

    category_column = _quote_identifier(schema["category"])
    brand_column = _quote_identifier(schema["brand"])
    price_column = _quote_identifier(schema["price"])

    where_clauses: list[str] = []
    params: list[Any] = []

    if filters.get("category"):
        where_clauses.append(
            f"LOWER(TRIM(CAST({category_column} AS TEXT))) = LOWER(TRIM(?))"
        )
        params.append(str(filters["category"]))

    if filters.get("budget") is not None:
        where_clauses.append(f"CAST({price_column} AS REAL) <= ?")
        params.append(float(filters["budget"]))

    for exclusion in filters.get("exclusions", []):
        where_clauses.append(
            f"LOWER(TRIM(CAST({brand_column} AS TEXT))) != LOWER(TRIM(?))"
        )
        params.append(str(exclusion))

    where_sql = (
        "WHERE " + " AND ".join(where_clauses)
        if where_clauses
        else ""
    )

    sql = f"""
        SELECT *
        FROM "{TABLE_NAME}"
        {where_sql}
        ORDER BY CAST({price_column} AS REAL) ASC
    """

    with get_connection() as connection:
        rows = connection.execute(sql, params).fetchall()

    return [dict(row) for row in rows]


def _first_product_value(
    product: dict[str, Any],
    canonical_field: str,
    default: Any = None,
) -> Any:
    """Read a canonical product value from any supported field alias."""
    aliases = FIELD_ALIASES.get(canonical_field, (canonical_field,))

    for key in (canonical_field, *aliases):
        if key in product and product[key] not in (None, ""):
            return product[key]

    return default


def _optional_float(value: Any) -> float | None:
    """Convert a value to float when possible without raising an exception."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _canonical_product(product: dict[str, Any]) -> dict[str, Any]:
    """
    Convert a database row into the stable product representation used by the
    ranking engine and API response.
    """
    product_id = _first_product_value(product, "product_id")
    category = str(
        _first_product_value(product, "category", "Unknown category")
    )
    brand = str(
        _first_product_value(product, "brand", "Unknown brand")
    )

    price = _optional_float(
        _first_product_value(product, "price")
    )

    if price is None:
        raise ValueError(
            f"Product {product_id!r} has an invalid price value."
        )

    product_name = _first_product_value(product, "product_name")

    if product_name is None:
        product_name = f"{brand} {category} #{product_id}"

    canonical = {
        "product_id": product_id,
        "product_name": str(product_name),
        "category": category,
        "brand": brand,
        "price": round(price, 2),
        "customer_age": _first_product_value(product, "customer_age"),
        "customer_gender": _first_product_value(product, "customer_gender"),
        "purchase_frequency": _first_product_value(product, "purchase_frequency"),
        "customer_satisfaction": _first_product_value(product, "customer_satisfaction"),
        "purchase_intent": _first_product_value(product, "purchase_intent"),
        "cpu": _first_product_value(product, "cpu"),
        "gpu": _first_product_value(product, "gpu"),
        "ram": _first_product_value(product, "ram"),
        "storage": _first_product_value(product, "storage"),
        "screen": _first_product_value(product, "screen"),
        "battery": _first_product_value(product, "battery"),
        "weight": _first_product_value(product, "weight"),
        "purchase_url": _first_product_value(product, "purchase_url"),
    }

    return canonical


# =============================================================================
# RECOMMENDATION ENGINE
# =============================================================================

def calculate_match_score(
    product: dict[str, Any],
    filters: dict[str, Any],
) -> tuple[int, list[str]]:
    """
    Calculate a bounded heuristic match score and explanation list.

    The score is a ranking heuristic, not a statistical probability. It combines
    explicit user constraints with behavioural indicators available in the
    original dataset. Missing optional indicators are ignored, allowing the
    engine to continue operating after the product database is redesigned.
    """
    canonical = _canonical_product(product)

    score = 35
    reasons: list[str] = []

    category = filters.get("category")
    if category:
        if canonical["category"].strip().lower() == str(category).strip().lower():
            score += 15
            reasons.append(f"matches category: {category}")
        else:
            score -= 15

    brand = filters.get("brand")
    if brand:
        if canonical["brand"].strip().lower() == str(brand).strip().lower():
            score += 15
            reasons.append(f"matches preferred brand: {brand}")
        else:
            score -= 3

    budget = filters.get("budget")
    if budget is not None:
        budget_value = float(budget)
        price = float(canonical["price"])

        if budget_value > 0 and price <= budget_value:
            price_ratio = price / budget_value
            ideal_ratio = 0.70

            price_score = round(
                12 - abs(price_ratio - ideal_ratio) * 15
            )
            price_score = max(4, min(12, price_score))

            score += price_score
            reasons.append(f"within budget ${budget_value:.0f}")

    satisfaction = _optional_float(canonical["customer_satisfaction"])
    if satisfaction is not None:
        # The current dataset uses a five-point satisfaction scale.
        satisfaction_bonus = round(
            max(0.0, min(5.0, satisfaction)) / 5.0 * 10
        )
        score += satisfaction_bonus

        if satisfaction >= 4:
            reasons.append("high customer satisfaction")

    purchase_frequency = _optional_float(canonical["purchase_frequency"])
    if purchase_frequency is not None:
        if purchase_frequency >= 7:
            score += 5
            reasons.append("strong purchase frequency")
        elif purchase_frequency >= 4:
            score += 2

    purchase_intent = _optional_float(canonical["purchase_intent"])
    if purchase_intent is not None and purchase_intent >= 1:
        score += 5
        reasons.append("positive purchase intent")

    bounded_score = max(0, min(100, int(round(score))))
    return bounded_score, reasons[:4]


def build_leaderboard(
    filters: dict[str, Any],
    limit: int = DEFAULT_RECOMMENDATION_LIMIT,
) -> list[dict[str, Any]]:
    """
    Build a ranked recommendation leaderboard using current database records.

    Optional hardware specification fields are included only when available.
    This allows the GitHub Pages comparison interface to progressively display
    richer data after the database redesign is merged.
    """
    candidates = fetch_candidate_products(filters)

    leaderboard: list[dict[str, Any]] = []

    for raw_product in candidates:
        canonical = _canonical_product(raw_product)
        score, reasons = calculate_match_score(raw_product, filters)

        item: dict[str, Any] = {
            "product_id": canonical["product_id"],
            "product_name": canonical["product_name"],
            "name": canonical["product_name"],
            "category": canonical["category"],
            "brand": canonical["brand"],
            "price": canonical["price"],
            "match_score": score,
            "reason": "; ".join(reasons) or "general product match",
        }

        optional_response_fields = (
            "cpu",
            "gpu",
            "ram",
            "storage",
            "screen",
            "battery",
            "weight",
            "purchase_url",
        )

        for field in optional_response_fields:
            value = canonical.get(field)
            if value not in (None, ""):
                item[field] = value

        leaderboard.append(item)

    # Higher match scores rank first. Price acts as a deterministic secondary
    # criterion, favouring the lower-priced product when scores are equal.
    leaderboard.sort(
        key=lambda item: (
            -item["match_score"],
            item["price"],
        )
    )

    safe_limit = max(
        0,
        min(MAX_RECOMMENDATION_LIMIT, int(limit)),
    )

    return leaderboard[:safe_limit]


# =============================================================================
# API ROUTES
# =============================================================================

@app.after_request
def add_api_response_headers(response):
    """
    Add small security and caching headers to API responses.

    Recommendation responses are generated dynamically and therefore should not
    be reused from an intermediary cache during demonstrations or testing.
    """
    if request.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"

    return response


@app.route("/api/health", methods=["GET"])
def health_check():
    """
    Return API and database health information.

    This endpoint is intentionally lightweight and can be used after deployment
    to distinguish frontend connectivity problems from backend availability
    problems.
    """
    row_count = setup_database()

    with get_connection() as connection:
        columns = _get_table_columns(connection)

    return jsonify(
        {
            "status": "success",
            "api_version": API_VERSION,
            "database": DB_PATH.name,
            "table": TABLE_NAME,
            "records": row_count,
            "columns": columns,
        }
    )


@app.route("/api/products", methods=["GET"])
def products():
    """
    Return a small normalised product sample for diagnostics and development.
    """
    setup_database()

    try:
        requested_limit = int(request.args.get("limit", 5))
    except ValueError as exc:
        raise APIError("'limit' must be an integer.", 400) from exc

    limit = max(1, min(20, requested_limit))

    schema = _active_schema()
    price_column = _quote_identifier(schema["price"])

    with get_connection() as connection:
        rows = connection.execute(
            f"""
            SELECT *
            FROM "{TABLE_NAME}"
            ORDER BY CAST({price_column} AS REAL) ASC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    data = []

    for row in rows:
        canonical = _canonical_product(dict(row))
        data.append(
            {
                "product_id": canonical["product_id"],
                "product_name": canonical["product_name"],
                "category": canonical["category"],
                "brand": canonical["brand"],
                "price": canonical["price"],
            }
        )

    return jsonify(
        {
            "status": "success",
            "data": data,
        }
    )


@app.route("/api/recommend", methods=["GET", "POST"])
def recommend():
    """
    Return ranked recommendations in the contract consumed by index.html.

    POST is the preferred production method. GET remains available so earlier
    automated tests and simple browser-based diagnostics continue to work.
    """
    filters = read_request_filters()
    limit = int(filters.pop("limit", DEFAULT_RECOMMENDATION_LIMIT))

    leaderboard = build_leaderboard(
        filters,
        limit=limit,
    )

    return jsonify(
        {
            "status": "success",
            "filters": filters,
            "data": leaderboard,
        }
    )


# =============================================================================
# ERROR HANDLERS
# =============================================================================

@app.errorhandler(APIError)
def handle_api_error(error: APIError):
    """Return a controlled client-facing API error."""
    return jsonify(
        {
            "status": "error",
            "message": error.message,
        }
    ), error.status_code


@app.errorhandler(FileNotFoundError)
def handle_missing_file(error: FileNotFoundError):
    """Return a JSON error when required bootstrap data is unavailable."""
    logger.error("Required data file missing: %s", error)

    return jsonify(
        {
            "status": "error",
            "message": str(error),
        }
    ), 500


@app.errorhandler(ValueError)
def handle_invalid_data(error: ValueError):
    """Return a JSON error when database or dataset structure is invalid."""
    logger.error("Invalid application data: %s", error)

    return jsonify(
        {
            "status": "error",
            "message": str(error),
        }
    ), 500


@app.errorhandler(sqlite3.Error)
def handle_database_error(error: sqlite3.Error):
    """
    Return a safe JSON response for database failures.

    Detailed SQLite information is written to server logs rather than sent to
    the browser, reducing unnecessary disclosure of internal implementation
    details.
    """
    logger.exception("Database operation failed.")

    return jsonify(
        {
            "status": "error",
            "message": "A database operation failed. Please try again later.",
        }
    ), 500


@app.errorhandler(404)
def handle_not_found(_error):
    """Return JSON for unknown backend routes."""
    return jsonify(
        {
            "status": "error",
            "message": "API endpoint not found.",
        }
    ), 404


@app.errorhandler(405)
def handle_method_not_allowed(_error):
    """Return JSON when an endpoint is called with an unsupported HTTP method."""
    return jsonify(
        {
            "status": "error",
            "message": "HTTP method not allowed for this endpoint.",
        }
    ), 405


@app.errorhandler(Exception)
def handle_unexpected_error(error: Exception):
    """
    Prevent unexpected exceptions from returning Flask's HTML error page.

    The full exception is retained in server logs for diagnosis while the client
    receives a stable and non-sensitive JSON response.
    """
    logger.exception("Unhandled backend exception: %s", error)

    return jsonify(
        {
            "status": "error",
            "message": "An unexpected server error occurred.",
        }
    ), 500


# =============================================================================
# LOCAL APPLICATION ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"

    logger.info("Starting recommendation API on http://%s:%s", host, port)
    logger.info(
        "GitHub Pages origin permitted by CORS: %s",
        GITHUB_PAGES_ORIGIN,
    )
    logger.info(
        "Health endpoint: http://%s:%s/api/health",
        host,
        port,
    )

    app.run(
        host=host,
        port=port,
        debug=debug,
    )
