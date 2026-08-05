"""CP3407 recommendation API with persistent accounts and search history.

Production uses PostgreSQL when DATABASE_URL is configured. Local development
falls back to the bundled SQLite database. The bundled SQLite file is also the
one-time source for the original 9,000 behavioural product rows.
"""

from __future__ import annotations

import csv
import json
import os
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import jwt
from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    UniqueConstraint,
    and_,
    create_engine,
    delete,
    func,
    insert,
    or_,
    select,
)
from sqlalchemy.engine import Engine
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = Path(__file__).resolve().parent
SQLITE_SEED_PATH = BASE_DIR / "digital_products.db"
SPECS_SEED_PATH = BASE_DIR / "product_specs.csv"
CATALOG_TARGET_COUNT = int(os.getenv("CATALOG_TARGET_COUNT", "2000"))
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
TOP_RECOMMENDATION_COUNT = 5
API_VERSION = "3.0.0-database-history"


class APIError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


def _database_url() -> str:
    configured = os.getenv("DATABASE_URL", "").strip()
    if configured.startswith("postgres://"):
        configured = "postgresql+psycopg://" + configured.removeprefix("postgres://")
    elif configured.startswith("postgresql://"):
        configured = "postgresql+psycopg://" + configured.removeprefix("postgresql://")
    if configured:
        return configured
    return f"sqlite:///{SQLITE_SEED_PATH}"


metadata = MetaData()

products_table = Table(
    "products",
    metadata,
    Column("ProductID", Integer, primary_key=True),
    Column("ProductCategory", String(80), nullable=False),
    Column("ProductBrand", String(100), nullable=False),
    Column("ProductPrice", Float, nullable=False),
    Column("CustomerAge", Integer),
    Column("CustomerGender", String(30)),
    Column("PurchaseFrequency", Integer),
    Column("CustomerSatisfaction", Integer),
    Column("PurchaseIntent", Integer),
)

product_specs_table = Table(
    "product_specs",
    metadata,
    Column("ProductID", Integer, ForeignKey("products.ProductID", ondelete="CASCADE"), primary_key=True),
    Column("ProductName", String(180), nullable=False),
    Column("CPU", String(160), nullable=False),
    Column("GPU", String(160), nullable=False),
    Column("RAM", String(80), nullable=False),
    Column("Storage", String(100), nullable=False),
    Column("ScreenSize", String(80), nullable=False),
    Column("BatteryLife", String(80), nullable=False),
    Column("Weight", String(80), nullable=False),
    Column("UseCase", String(240), nullable=False),
    Column("PurchaseURL", Text, nullable=False),
    Column("DataSource", String(80), nullable=False, default="educational-prototype"),
    Column("LastUpdated", DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),
)

users_table = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(80), nullable=False, unique=True),
    Column("email", String(255), nullable=False, unique=True),
    Column("password_hash", String(255), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),
)

favorites_table = Table(
    "favorites",
    metadata,
    Column("favorite_id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
    Column("product_id", Integer, ForeignKey("products.ProductID", ondelete="CASCADE"), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),
    UniqueConstraint("user_id", "product_id", name="uq_favorite_user_product"),
)

search_history_table = Table(
    "search_history",
    metadata,
    Column("history_id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
    Column("query_text", Text, nullable=False),
    Column("filters_json", Text, nullable=False),
    Column("total_candidates", Integer, nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),
)

search_results_table = Table(
    "search_results",
    metadata,
    Column("result_id", Integer, primary_key=True, autoincrement=True),
    Column("history_id", Integer, ForeignKey("search_history.history_id", ondelete="CASCADE"), nullable=False),
    Column("product_id", Integer, ForeignKey("products.ProductID"), nullable=False),
    Column("rank", Integer, nullable=False),
    Column("match_score", Integer, nullable=False),
    Column("reason", Text, nullable=False),
    Column("snapshot_json", Text, nullable=False),
)

feedback_table = Table(
    "feedback",
    metadata,
    Column("feedback_id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="SET NULL")),
    Column("history_id", Integer, ForeignKey("search_history.history_id", ondelete="SET NULL")),
    Column("vote", String(10), nullable=False),
    Column("query_text", Text, nullable=False, default=""),
    Column("top_product_id", Integer, ForeignKey("products.ProductID", ondelete="SET NULL")),
    Column("created_at", DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)),
)

engine: Engine = create_engine(_database_url(), future=True, pool_pre_ping=True)


def configure_database(database_url: str) -> None:
    """Switch database targets cleanly for tests and local administration."""
    global engine
    engine.dispose()
    engine = create_engine(database_url, future=True, pool_pre_ping=True)

app = Flask(__name__)
CORS(
    app,
    origins=[
        "https://chu-junjie.github.io",
        "https://tiantian09091.github.io",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "DELETE", "OPTIONS"],
)


def _rows_from_bundled_sqlite() -> list[dict[str, Any]]:
    if not SQLITE_SEED_PATH.exists():
        return []
    connection = sqlite3.connect(SQLITE_SEED_PATH)
    connection.row_factory = sqlite3.Row
    try:
        exists = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='products'"
        ).fetchone()
        if not exists:
            return []
        return [dict(row) for row in connection.execute("SELECT * FROM products").fetchall()]
    finally:
        connection.close()


def _prototype_specs() -> list[dict[str, Any]]:
    if not SPECS_SEED_PATH.exists():
        return []
    with SPECS_SEED_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _manufacturer_url(brand: str) -> str:
    urls = {
        "apple": "https://www.apple.com/",
        "samsung": "https://www.samsung.com/",
        "sony": "https://www.sony.com/",
        "hp": "https://www.hp.com/",
    }
    return urls.get(brand.lower(), "https://www.google.com/search?q=digital+product")


def _synthetic_spec(product: dict[str, Any], sequence: int) -> dict[str, Any]:
    """Create deterministic, honestly-labelled educational catalogue coverage."""
    product_id = int(product["ProductID"])
    category = str(product["ProductCategory"])
    brand = str(product["ProductBrand"])
    variants = product_id % 5
    if category == "Laptops":
        fields = (f"Intel Core i{5 + (variants % 3) * 2}", "Integrated Graphics", f"{8 + variants * 4}GB", f"{256 + variants * 128}GB SSD", f"{13 + variants * 0.7:.1f} inch", f"{7 + variants} hours", f"{1.2 + variants * 0.18:.2f} kg", "study office portable creative")
    elif category == "Smartphones":
        fields = (f"Mobile Processor Gen {variants + 1}", "Mobile GPU", f"{4 + variants * 2}GB", f"{64 + variants * 64}GB", f"{5.8 + variants * 0.2:.1f} inch", f"{18 + variants * 2} hours", f"{0.16 + variants * 0.01:.2f} kg", "camera video portable battery")
    elif category == "Tablets":
        fields = (f"Tablet Processor Gen {variants + 1}", "Tablet GPU", f"{4 + variants * 2}GB", f"{64 + variants * 64}GB", f"{9 + variants * 0.6:.1f} inch", f"{9 + variants} hours", f"{0.42 + variants * 0.05:.2f} kg", "study creative portable media")
    elif category == "Headphones":
        fields = ("Not applicable", "Not applicable", "Not applicable", "Not applicable", "Not applicable", f"{20 + variants * 5} hours", f"{0.20 + variants * 0.02:.2f} kg", "music travel office battery")
    else:
        fields = (f"Wearable Processor Gen {variants + 1}", "Wearable GPU", f"{1 + variants}GB", f"{16 + variants * 8}GB", f"{1.4 + variants * 0.1:.1f} inch", f"{18 + variants * 6} hours", f"{0.04 + variants * 0.01:.2f} kg", "fitness travel notifications battery")
    cpu, gpu, ram, storage, screen, battery, weight, use_case = fields
    safe_category = category.rstrip("s").replace(" ", "-")
    return {
        "ProductID": product_id,
        "ProductName": f"{brand} {safe_category} EDU-{sequence:04d}",
        "CPU": cpu,
        "GPU": gpu,
        "RAM": ram,
        "Storage": storage,
        "ScreenSize": screen,
        "BatteryLife": battery,
        "Weight": weight,
        "UseCase": use_case,
        "PurchaseURL": _manufacturer_url(brand),
        "DataSource": "educational-synthetic",
        "LastUpdated": datetime.now(timezone.utc),
    }


def setup_database() -> dict[str, int]:
    metadata.create_all(engine)
    with engine.begin() as connection:
        product_count = int(connection.scalar(select(func.count()).select_from(products_table)) or 0)
        if product_count == 0:
            rows = _rows_from_bundled_sqlite()
            if not rows:
                raise RuntimeError("No product seed data is available.")
            for start in range(0, len(rows), 500):
                connection.execute(insert(products_table), rows[start : start + 500])

        spec_count = int(connection.scalar(select(func.count()).select_from(product_specs_table)) or 0)
        if spec_count == 0:
            product_ids = set(connection.scalars(select(products_table.c.ProductID)).all())
            prototypes: list[dict[str, Any]] = []
            for row in _prototype_specs():
                product_id = int(row["ProductID"])
                if product_id not in product_ids:
                    continue
                row["ProductID"] = product_id
                row["DataSource"] = "educational-prototype"
                row["LastUpdated"] = datetime.now(timezone.utc)
                prototypes.append(row)
            if prototypes:
                connection.execute(insert(product_specs_table), prototypes)

            existing = set(connection.scalars(select(product_specs_table.c.ProductID)).all())
            needed = max(0, min(CATALOG_TARGET_COUNT, len(product_ids)) - len(existing))
            candidates = connection.execute(
                select(products_table).where(products_table.c.ProductID.not_in(existing)).order_by(products_table.c.ProductID).limit(needed)
            ).mappings().all()
            generated = [_synthetic_spec(dict(row), index + 1) for index, row in enumerate(candidates)]
            for start in range(0, len(generated), 500):
                connection.execute(insert(product_specs_table), generated[start : start + 500])

        return {
            "products": int(connection.scalar(select(func.count()).select_from(products_table)) or 0),
            "product_specs": int(connection.scalar(select(func.count()).select_from(product_specs_table)) or 0),
            "users": int(connection.scalar(select(func.count()).select_from(users_table)) or 0),
            "favorites": int(connection.scalar(select(func.count()).select_from(favorites_table)) or 0),
            "search_history": int(connection.scalar(select(func.count()).select_from(search_history_table)) or 0),
            "feedback": int(connection.scalar(select(func.count()).select_from(feedback_table)) or 0),
        }


def parse_budget_from_text(text: str | None) -> float | None:
    if not text:
        return None
    value = str(text).lower().replace(",", "")
    patterns = [
        r"(?:under|below|less\s+than|budget(?:\s+(?:of|is))?|around|up\s+to|maximum|max|limit(?:\s+is)?)\s*\$?\s*(\d+(?:\.\d+)?)",
        r"\$\s*(\d+(?:\.\d+)?)",
    ]
    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            return float(match.group(1))
    return None


def parse_exclusions(text: str | None) -> list[str]:
    if not text:
        return []
    return list(dict.fromkeys(match.strip() for match in re.findall(r"\b(?:no|exclude|without)\s+([a-zA-Z0-9_-]+)\b", str(text), re.I)))


def parse_use_case_keywords(text: str | None) -> list[str]:
    lowered = str(text or "").lower()
    mapping = {
        "gaming": ["gaming", "game", "play"],
        "study": ["study", "student", "school", "university"],
        "office": ["office", "work", "business", "productivity"],
        "portable": ["portable", "light", "travel", "thin"],
        "battery": ["battery", "long lasting", "long-lasting", "durable"],
        "creative": ["creative", "video editing", "design"],
        "3d": ["3d", "modelling", "modeling", "render"],
        "camera": ["camera", "photo", "video"],
        "budget": ["cheap", "budget", "affordable", "value"],
    }
    return [label for label, phrases in mapping.items() if any(phrase in lowered for phrase in phrases)]


def infer_category_from_text(text: str | None) -> str | None:
    lowered = str(text or "").lower()
    aliases = {
        "Laptops": ["laptop", "notebook", "computer", "macbook"],
        "Smartphones": ["smartphone", "phone", "mobile", "android", "iphone"],
        "Tablets": ["tablet", "ipad"],
        "Headphones": ["headphone", "headset", "earphone", "earbud"],
        "Smart Watches": ["smart watch", "smartwatch", "watch"],
    }
    return next((category for category, words in aliases.items() if any(word in lowered for word in words)), None)


def infer_brand_from_text(text: str | None, exclusions: list[str] | None = None) -> str | None:
    lowered = str(text or "").lower()
    excluded = {value.lower() for value in exclusions or []}
    for brand in ["Apple", "Samsung", "HP", "Sony"]:
        if brand.lower() in lowered and brand.lower() not in excluded:
            return brand
    return None


def _positive_int(value: Any, default: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        parsed = default
    return max(1, min(maximum, parsed))


def read_request_filters() -> dict[str, Any]:
    payload = request.get_json(silent=True) or {} if request.method == "POST" else request.args.to_dict()
    query = str(payload.get("query") or payload.get("intent") or "").strip()
    exclusions = parse_exclusions(query)
    explicit_exclusions = payload.get("excluded_brands") or payload.get("exclusions") or []
    if isinstance(explicit_exclusions, str):
        explicit_exclusions = [item.strip() for item in explicit_exclusions.split(",") if item.strip()]
    exclusions = list(dict.fromkeys([*exclusions, *explicit_exclusions]))
    category = str(payload.get("category") or "").strip() or infer_category_from_text(query)
    brand = str(payload.get("brand") or "").strip() or infer_brand_from_text(query, exclusions)
    budget_raw = payload.get("max_price", payload.get("budget"))
    try:
        budget = float(budget_raw) if budget_raw not in (None, "") else parse_budget_from_text(query)
    except (TypeError, ValueError):
        raise APIError("max_price must be a number.")
    if budget is not None and budget <= 0:
        raise APIError("max_price must be greater than zero.")
    return {
        "query": query,
        "category": category or None,
        "brand": brand or None,
        "budget": budget,
        "max_price": budget,
        "exclusions": exclusions,
        "excluded_brands": exclusions,
        "use_cases": parse_use_case_keywords(query),
        "page": _positive_int(payload.get("page"), 1, 100000),
        "per_page": _positive_int(payload.get("per_page", payload.get("limit")), DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE),
        "save_history": payload.get("save_history", True) is not False,
    }


def _joined_rows(filters: dict[str, Any]) -> list[dict[str, Any]]:
    statement = select(products_table, product_specs_table).join(
        product_specs_table, products_table.c.ProductID == product_specs_table.c.ProductID
    )
    conditions = []
    if filters.get("category"):
        conditions.append(func.lower(products_table.c.ProductCategory) == str(filters["category"]).lower())
    if filters.get("budget") is not None:
        conditions.append(products_table.c.ProductPrice <= float(filters["budget"]))
    for excluded in filters.get("exclusions", []):
        conditions.append(func.lower(products_table.c.ProductBrand) != str(excluded).lower())
    if conditions:
        statement = statement.where(and_(*conditions))
    with engine.connect() as connection:
        return [dict(row) for row in connection.execute(statement).mappings().all()]


def calculate_match_score(product: dict[str, Any], filters: dict[str, Any]) -> tuple[int, list[str]]:
    score = 10
    reasons: list[str] = []
    if filters.get("category") and str(product["ProductCategory"]).lower() == str(filters["category"]).lower():
        score += 22
        reasons.append(f"matches category: {filters['category']}")
    if filters.get("brand"):
        if str(product["ProductBrand"]).lower() == str(filters["brand"]).lower():
            score += 18
            reasons.append(f"matches preferred brand: {filters['brand']}")
        else:
            score -= 5
    if filters.get("budget") is not None:
        score += 12
        reasons.append(f"within budget ${float(filters['budget']):.0f}")
    use_case_text = str(product.get("UseCase") or "").lower()
    matches = [label for label in filters.get("use_cases", []) if label in use_case_text]
    if matches:
        score += min(15, len(matches) * 5)
        reasons.append("fits " + ", ".join(matches))
    satisfaction = int(product.get("CustomerSatisfaction") or 0)
    score += max(0, min(10, satisfaction * 2))
    if satisfaction >= 4:
        reasons.append("high customer satisfaction")
    if int(product.get("PurchaseFrequency") or 0) >= 7:
        score += 5
        reasons.append("strong purchase frequency")
    if int(product.get("PurchaseIntent") or 0) >= 1:
        score += 4
        reasons.append("positive purchase intent")
    return max(0, min(100, score)), reasons[:5]


def product_payload(product: dict[str, Any], score: int | None = None, reason: str | None = None) -> dict[str, Any]:
    result = {
        "product_id": int(product["ProductID"]),
        "id": int(product["ProductID"]),
        "product_name": product["ProductName"],
        "name": product["ProductName"],
        "category": product["ProductCategory"],
        "brand": product["ProductBrand"],
        "price": round(float(product["ProductPrice"]), 2),
        "cpu": product["CPU"],
        "gpu": product["GPU"],
        "ram": product["RAM"],
        "storage": product["Storage"],
        "screen_size": product["ScreenSize"],
        "battery_life": product["BatteryLife"],
        "weight": product["Weight"],
        "use_case": product["UseCase"],
        "purchase_url": product["PurchaseURL"],
        "data_source": product.get("DataSource", "educational-prototype"),
    }
    if score is not None:
        result["match_score"] = score
        result["score"] = score
    if reason is not None:
        result["reason"] = reason
    return result


def build_leaderboard(filters: dict[str, Any], limit: int | None = None) -> list[dict[str, Any]]:
    items = []
    for product in _joined_rows(filters):
        score, reasons = calculate_match_score(product, filters)
        items.append(product_payload(product, score, "; ".join(reasons) or "general product match"))
    items.sort(key=lambda item: (-int(item["match_score"]), float(item["price"])))
    return items[:limit] if limit is not None else items


def _jwt_secret() -> str:
    return os.getenv("JWT_SECRET_KEY", "local-development-change-me-32-bytes-minimum")


def _issue_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    return jwt.encode({"sub": str(user_id), "iat": now, "exp": now + timedelta(days=7)}, _jwt_secret(), algorithm="HS256")


def _current_user_id(required: bool = False) -> int | None:
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        if required:
            raise APIError("Login is required.", 401)
        return None
    try:
        payload = jwt.decode(header.removeprefix("Bearer ").strip(), _jwt_secret(), algorithms=["HS256"])
        return int(payload["sub"])
    except (jwt.PyJWTError, KeyError, TypeError, ValueError) as exc:
        if required:
            raise APIError("The login session is invalid or expired.", 401) from exc
        return None


def _save_history(user_id: int, filters: dict[str, Any], total: int, results: list[dict[str, Any]]) -> int:
    clean_filters = {key: value for key, value in filters.items() if key not in {"page", "per_page", "save_history"}}
    with engine.begin() as connection:
        result = connection.execute(
            insert(search_history_table).values(
                user_id=user_id,
                query_text=filters.get("query") or "Product search",
                filters_json=json.dumps(clean_filters),
                total_candidates=total,
                created_at=datetime.now(timezone.utc),
            )
        )
        history_id = int(result.inserted_primary_key[0])
        rows = [
            {
                "history_id": history_id,
                "product_id": item["product_id"],
                "rank": rank,
                "match_score": item["match_score"],
                "reason": item["reason"],
                "snapshot_json": json.dumps(item),
            }
            for rank, item in enumerate(results[:MAX_PAGE_SIZE], 1)
        ]
        if rows:
            connection.execute(insert(search_results_table), rows)
        return history_id


@app.get("/")
def api_home():
    return jsonify({"status": "success", "message": "Smart Digital Product Recommendation API is running.", "api_version": API_VERSION, "database": engine.url.get_backend_name(), "endpoints": {"health": "/api/health", "register": "/api/auth/register", "login": "/api/auth/login", "recommend": "/api/recommend", "history": "/api/history", "favorites": "/api/favorites", "compare": "/api/compare", "feedback": "/api/feedback"}})


@app.get("/api/health")
def health():
    counts = setup_database()
    return jsonify({"status": "success", "api_version": API_VERSION, "database": engine.url.get_backend_name(), "tables": counts, "joined_recommendation_candidates": counts["product_specs"], "notes": "Product catalogue includes explicitly labelled educational prototype and synthetic records; prices are not live retail prices."})


@app.post("/api/auth/register")
def register():
    setup_database()
    payload = request.get_json(silent=True) or {}
    username = str(payload.get("username") or "").strip()
    email = str(payload.get("email") or "").strip().lower()
    password = str(payload.get("password") or "")
    if len(username) < 3 or "@" not in email or len(password) < 8:
        raise APIError("Username must have 3 characters, email must be valid, and password must have at least 8 characters.")
    with engine.begin() as connection:
        exists = connection.execute(select(users_table.c.user_id).where(or_(func.lower(users_table.c.username) == username.lower(), func.lower(users_table.c.email) == email))).first()
        if exists:
            raise APIError("Username or email already exists.", 409)
        result = connection.execute(insert(users_table).values(username=username, email=email, password_hash=generate_password_hash(password), created_at=datetime.now(timezone.utc)))
        user_id = int(result.inserted_primary_key[0])
    return jsonify({"status": "success", "token": _issue_token(user_id), "user": {"user_id": user_id, "username": username, "email": email}}), 201


@app.post("/api/auth/login")
def login():
    setup_database()
    payload = request.get_json(silent=True) or {}
    identifier = str(payload.get("identifier") or payload.get("email") or payload.get("username") or "").strip().lower()
    password = str(payload.get("password") or "")
    with engine.connect() as connection:
        user = connection.execute(select(users_table).where(or_(func.lower(users_table.c.username) == identifier, func.lower(users_table.c.email) == identifier))).mappings().first()
    if not user or not check_password_hash(user["password_hash"], password):
        raise APIError("Invalid username/email or password.", 401)
    return jsonify({"status": "success", "token": _issue_token(int(user["user_id"])), "user": {"user_id": user["user_id"], "username": user["username"], "email": user["email"]}})


@app.get("/api/auth/me")
def me():
    setup_database()
    user_id = _current_user_id(required=True)
    with engine.connect() as connection:
        user = connection.execute(select(users_table.c.user_id, users_table.c.username, users_table.c.email, users_table.c.created_at).where(users_table.c.user_id == user_id)).mappings().first()
    if not user:
        raise APIError("User no longer exists.", 401)
    return jsonify({"status": "success", "user": dict(user)})


@app.route("/api/recommend", methods=["GET", "POST"])
def recommend():
    setup_database()
    filters = read_request_filters()
    all_results = build_leaderboard(filters)
    total = len(all_results)
    page, per_page = filters["page"], filters["per_page"]
    start = (page - 1) * per_page
    page_results = all_results[start : start + per_page]
    history_id = None
    user_id = _current_user_id()
    if user_id and page == 1 and filters["save_history"]:
        history_id = _save_history(user_id, filters, total, page_results)
    response_filters = {key: value for key, value in filters.items() if key not in {"page", "per_page", "save_history"}}
    return jsonify({"status": "success", "message": f"Found {total} matching products.", "filters": response_filters, "count": len(page_results), "total_candidates": total, "page": page, "per_page": per_page, "total_pages": (total + per_page - 1) // per_page if total else 0, "top_recommendations": all_results[:TOP_RECOMMENDATION_COUNT], "data": page_results, "history_id": history_id})


@app.get("/api/products")
def products():
    setup_database()
    filters = read_request_filters()
    rows = build_leaderboard(filters)
    page, per_page = filters["page"], filters["per_page"]
    start = (page - 1) * per_page
    return jsonify({"status": "success", "total": len(rows), "page": page, "per_page": per_page, "data": rows[start : start + per_page]})


@app.get("/api/history")
def history_list():
    setup_database()
    user_id = _current_user_id(required=True)
    page = _positive_int(request.args.get("page"), 1, 100000)
    per_page = _positive_int(request.args.get("per_page"), 20, 100)
    with engine.connect() as connection:
        total = int(connection.scalar(select(func.count()).select_from(search_history_table).where(search_history_table.c.user_id == user_id)) or 0)
        rows = connection.execute(select(search_history_table).where(search_history_table.c.user_id == user_id).order_by(search_history_table.c.created_at.desc()).offset((page - 1) * per_page).limit(per_page)).mappings().all()
    return jsonify({"status": "success", "total": total, "page": page, "per_page": per_page, "data": [{**dict(row), "filters": json.loads(row["filters_json"])} for row in rows]})


@app.route("/api/history/<int:history_id>", methods=["GET", "DELETE"])
def history_detail(history_id: int):
    setup_database()
    user_id = _current_user_id(required=True)
    with engine.begin() as connection:
        record = connection.execute(select(search_history_table).where(and_(search_history_table.c.history_id == history_id, search_history_table.c.user_id == user_id))).mappings().first()
        if not record:
            raise APIError("History record not found.", 404)
        if request.method == "DELETE":
            connection.execute(delete(search_results_table).where(search_results_table.c.history_id == history_id))
            connection.execute(delete(search_history_table).where(search_history_table.c.history_id == history_id))
            return jsonify({"status": "success", "message": "History record deleted."})
        results = connection.execute(select(search_results_table).where(search_results_table.c.history_id == history_id).order_by(search_results_table.c.rank)).mappings().all()
    return jsonify({"status": "success", "history": {**dict(record), "filters": json.loads(record["filters_json"])}, "data": [json.loads(row["snapshot_json"]) for row in results]})


@app.route("/api/favorites", methods=["GET", "POST"])
def favorites():
    setup_database()
    user_id = _current_user_id(required=True)
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
        try:
            product_id = int(payload.get("product_id"))
        except (TypeError, ValueError):
            raise APIError("product_id must be an integer.")
        with engine.begin() as connection:
            product = connection.execute(
                select(products_table.c.ProductID)
                .join(product_specs_table, products_table.c.ProductID == product_specs_table.c.ProductID)
                .where(products_table.c.ProductID == product_id)
            ).first()
            if not product:
                raise APIError("Product not found.", 404)
            exists = connection.execute(
                select(favorites_table.c.favorite_id).where(
                    and_(favorites_table.c.user_id == user_id, favorites_table.c.product_id == product_id)
                )
            ).first()
            if exists:
                return jsonify({"status": "success", "message": "Product is already in favorites.", "favorite_id": exists[0]})
            result = connection.execute(insert(favorites_table).values(
                user_id=user_id, product_id=product_id, created_at=datetime.now(timezone.utc)
            ))
            favorite_id = int(result.inserted_primary_key[0])
        return jsonify({"status": "success", "message": "Product added to favorites.", "favorite_id": favorite_id}), 201

    category = str(request.args.get("category") or "").strip()
    statement = (
        select(products_table, product_specs_table, favorites_table.c.favorite_id, favorites_table.c.created_at.label("favorited_at"))
        .select_from(
            favorites_table.join(products_table, favorites_table.c.product_id == products_table.c.ProductID)
            .join(product_specs_table, products_table.c.ProductID == product_specs_table.c.ProductID)
        )
        .where(favorites_table.c.user_id == user_id)
        .order_by(products_table.c.ProductCategory, favorites_table.c.created_at.desc())
    )
    if category:
        statement = statement.where(func.lower(products_table.c.ProductCategory) == category.lower())
    with engine.connect() as connection:
        rows = connection.execute(statement).mappings().all()
    data = []
    for row in rows:
        item = product_payload(dict(row))
        item["favorite_id"] = int(row["favorite_id"])
        item["favorited_at"] = row["favorited_at"]
        data.append(item)
    return jsonify({"status": "success", "count": len(data), "data": data})


@app.delete("/api/favorites/<int:product_id>")
def delete_favorite(product_id: int):
    setup_database()
    user_id = _current_user_id(required=True)
    with engine.begin() as connection:
        result = connection.execute(delete(favorites_table).where(
            and_(favorites_table.c.user_id == user_id, favorites_table.c.product_id == product_id)
        ))
    if not result.rowcount:
        raise APIError("Favorite not found.", 404)
    return jsonify({"status": "success", "message": "Favorite removed."})


@app.post("/api/favorites/compare")
def compare_favorites():
    setup_database()
    user_id = _current_user_id(required=True)
    ids = _compare_ids()
    statement = (
        select(products_table, product_specs_table)
        .select_from(
            favorites_table.join(products_table, favorites_table.c.product_id == products_table.c.ProductID)
            .join(product_specs_table, products_table.c.ProductID == product_specs_table.c.ProductID)
        )
        .where(and_(favorites_table.c.user_id == user_id, products_table.c.ProductID.in_(ids)))
    )
    with engine.connect() as connection:
        rows = {int(row["ProductID"]): dict(row) for row in connection.execute(statement).mappings().all()}
    if len(rows) != len(ids):
        raise APIError("Every selected product must be in your favorites.", 400)
    categories = {str(row["ProductCategory"]) for row in rows.values()}
    if len(categories) != 1:
        raise APIError("Favorite comparison requires products from the same category.")
    return jsonify({"status": "success", "category": next(iter(categories)), "count": len(ids), "data": [product_payload(rows[value]) for value in ids]})


def _compare_ids() -> list[int]:
    payload = request.get_json(silent=True) or {} if request.method == "POST" else request.args
    raw = payload.get("product_ids", payload.get("ids", []))
    if isinstance(raw, str):
        raw = [part.strip() for part in raw.split(",") if part.strip()]
    try:
        ids = [int(value) for value in raw]
    except (TypeError, ValueError):
        raise APIError("product_ids must contain integers.")
    if len(ids) not in (2, 3) or len(set(ids)) != len(ids):
        raise APIError("Select exactly 2 or 3 unique products.")
    return ids


@app.route("/api/compare", methods=["GET", "POST"])
def compare():
    setup_database()
    ids = _compare_ids()
    statement = select(products_table, product_specs_table).join(product_specs_table).where(products_table.c.ProductID.in_(ids))
    with engine.connect() as connection:
        rows = {int(row["ProductID"]): dict(row) for row in connection.execute(statement).mappings().all()}
    missing = [value for value in ids if value not in rows]
    if missing:
        raise APIError(f"Products not found: {missing}")
    data = [product_payload(rows[value]) for value in ids]
    return jsonify({"status": "success", "requested_ids": ids, "count": len(data), "data": data})


@app.route("/api/feedback", methods=["GET", "POST"])
def feedback():
    setup_database()
    if request.method == "GET":
        with engine.connect() as connection:
            rows = connection.execute(select(feedback_table.c.vote, func.count().label("count")).group_by(feedback_table.c.vote)).all()
        summary = {"up": 0, "down": 0}
        for vote, count in rows:
            summary[vote] = int(count)
        return jsonify({"status": "success", "data": {**summary, "total": summary["up"] + summary["down"]}})
    payload = request.get_json(silent=True) or {}
    vote = str(payload.get("vote") or "").lower()
    if vote not in {"up", "down"}:
        raise APIError("vote must be 'up' or 'down'.")
    user_id = _current_user_id()
    with engine.begin() as connection:
        result = connection.execute(insert(feedback_table).values(user_id=user_id, history_id=payload.get("history_id"), vote=vote, query_text=str(payload.get("query") or ""), top_product_id=payload.get("top_product_id"), created_at=datetime.now(timezone.utc)))
        feedback_id = int(result.inserted_primary_key[0])
    return jsonify({"status": "success", "message": "Feedback saved.", "feedback_id": feedback_id}), 201


@app.errorhandler(APIError)
def handle_api_error(error: APIError):
    return jsonify({"status": "error", "message": error.message}), error.status_code


@app.errorhandler(Exception)
def handle_unexpected_error(error: Exception):
    app.logger.exception("Unhandled API error")
    return jsonify({"status": "error", "message": "An internal server error occurred."}), 500


@app.after_request
def response_headers(response):
    if request.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
    return response


if __name__ == "__main__":
    setup_database()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
