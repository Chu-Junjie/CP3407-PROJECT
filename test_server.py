from pathlib import Path

import pandas as pd
import pytest

import server


# ============================================================
# TEST DATA AND FIXTURES
# ============================================================

@pytest.fixture(autouse=True)
def isolated_database(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Use a temporary CSV and SQLite database for every test."""
    csv_path = tmp_path / "US-02 Database Setup & Import.csv"
    db_path = tmp_path / "digital_products.db"

    dataframe = pd.DataFrame(
        [
            [1, "Laptops", "Apple", 900, 22, "Female", 8, 5, 1],
            [2, "Laptops", "HP", 700, 30, "Male", 6, 4, 1],
            [3, "Laptops", "Samsung", 1100, 26, "Female", 4, 4, 1],
            [4, "Smartphones", "Apple", 800, 24, "Male", 7, 5, 1],
            [5, "Smartphones", "Samsung", 600, 35, "Female", 5, 4, 1],
            [6, "Tablets", "Sony", 500, 28, "Male", 3, 3, 0],
            [7, "Headphones", "Sony", 250, 19, "Female", 9, 5, 1],
        ],
        columns=[
            "ProductID",
            "ProductCategory",
            "ProductBrand",
            "ProductPrice",
            "CustomerAge",
            "CustomerGender",
            "PurchaseFrequency",
            "CustomerSatisfaction",
            "PurchaseIntent",
        ],
    )
    dataframe.to_csv(csv_path, index=False)

    monkeypatch.setattr(server, "CSV_PATH", csv_path)
    monkeypatch.setattr(server, "DB_PATH", db_path)

    yield


@pytest.fixture
def client():
    """Create a Flask test client."""
    server.app.config["TESTING"] = True
    with server.app.test_client() as test_client:
        yield test_client


@pytest.fixture
def sample_product():
    return {
        "ProductID": 1,
        "ProductCategory": "Laptops",
        "ProductBrand": "Apple",
        "ProductPrice": 900,
        "CustomerAge": 22,
        "CustomerGender": "Female",
        "PurchaseFrequency": 8,
        "CustomerSatisfaction": 5,
        "PurchaseIntent": 1,
    }


# ============================================================
# US-01: NATURAL-LANGUAGE BUDGET PROCESSING
# ============================================================

def test_us01_parse_explicit_budget():
    """TC-01.1: Extract an explicit budget."""
    result = server.parse_budget_from_text(
        "I need a gaming laptop under $1200"
    )
    assert result == 1200.0


def test_us01_parse_no_budget():
    """TC-01.2: Return None when no budget is provided."""
    result = server.parse_budget_from_text(
        "Just give me the best laptop"
    )
    assert result is None


def test_us01_parse_budget_with_comma():
    """TC-01.3: Extract a budget containing a comma."""
    result = server.parse_budget_from_text(
        "My maximum budget is $1,500"
    )
    assert result == 1500.0


# ============================================================
# US-02: DATABASE SETUP AND INTEGRATION
# ============================================================

def test_us02_database_setup_imports_rows():
    """TC-02.1: Import product rows into a new database."""
    row_count = server.setup_database()
    assert row_count == 7


def test_us02_database_setup_does_not_duplicate_rows():
    """TC-02.2: Re-running setup does not duplicate products."""
    first_count = server.setup_database()
    second_count = server.setup_database()
    assert first_count == 7
    assert second_count == 7


def test_us02_health_endpoint_reports_database(client):
    """TC-02.3: Health endpoint returns database information."""
    response = client.get("/api/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["table"] == server.TABLE_NAME
    assert data["records"] == 7


# ============================================================
# US-03: REQUEST FILTER PROCESSING
# ============================================================

def test_us03_process_post_filters(client):
    """TC-03.1: Read category, brand, and max_price from POST JSON."""
    response = client.post(
        "/api/recommend",
        json={
            "query": "Find an Apple laptop",
            "category": "Laptops",
            "brand": "Apple",
            "max_price": 1000,
        },
    )
    filters = response.get_json()["filters"]

    assert filters == {
        "query": "Find an Apple laptop",
        "category": "Laptops",
        "brand": "Apple",
        "budget": 1000.0,
    }


def test_us03_accept_intent_as_query(client):
    """TC-03.2: Accept the earlier 'intent' field and parse its budget."""
    response = client.post(
        "/api/recommend",
        json={"intent": "I need a laptop below $850"},
    )
    filters = response.get_json()["filters"]

    assert filters["query"] == "I need a laptop below $850"
    assert filters["budget"] == 850.0


def test_us03_invalid_max_price_falls_back_to_query(client):
    """TC-03.3: Invalid max_price falls back to the natural-language query."""
    response = client.post(
        "/api/recommend",
        json={
            "query": "My budget is 900",
            "max_price": "not-a-number",
        },
    )
    filters = response.get_json()["filters"]

    assert filters["budget"] == 900.0


# ============================================================
# US-04: MATCH SCORING AND EXPLANATIONS
# ============================================================

def test_us04_match_score_is_between_zero_and_one_hundred(sample_product):
    """TC-04.1: A match score always remains in the valid range."""
    filters = {
        "query": "",
        "category": "Laptops",
        "brand": "Apple",
        "budget": 1000.0,
    }

    score, reasons = server.calculate_match_score(sample_product, filters)

    assert 0 <= score <= 100
    assert isinstance(reasons, list)


def test_us04_matching_preferences_receive_higher_score(sample_product):
    """TC-04.2: Matching preferences produce a higher score."""
    matching_filters = {
        "query": "",
        "category": "Laptops",
        "brand": "Apple",
        "budget": 1000.0,
    }
    non_matching_filters = {
        "query": "",
        "category": "Smartphones",
        "brand": "Samsung",
        "budget": 1000.0,
    }

    matching_score, _ = server.calculate_match_score(
        sample_product, matching_filters
    )
    non_matching_score, _ = server.calculate_match_score(
        sample_product, non_matching_filters
    )

    assert matching_score > non_matching_score


def test_us04_reasons_describe_matching_preferences(sample_product):
    """TC-04.3: Reasons explain category, brand, and budget matches."""
    filters = {
        "query": "",
        "category": "Laptops",
        "brand": "Apple",
        "budget": 1000.0,
    }

    _, reasons = server.calculate_match_score(sample_product, filters)
    combined = " ".join(reasons).lower()

    assert "matches category" in combined
    assert "matches brand" in combined
    assert "within budget" in combined


# ============================================================
# US-05: LEADERBOARD AND API OUTPUT
# ============================================================

def test_us05_candidates_never_exceed_maximum_budget():
    """TC-05.1: Strict budget filtering removes over-budget products."""
    server.setup_database()
    filters = {
        "query": "",
        "category": None,
        "brand": None,
        "budget": 1000.0,
    }

    candidates = server.fetch_candidate_products(filters)

    assert candidates
    assert all(
        float(product["ProductPrice"]) <= 1000.0
        for product in candidates
    )


def test_us05_leaderboard_contains_at_most_five_sorted_items():
    """TC-05.2: Leaderboard returns at most five items sorted by score."""
    filters = {
        "query": "",
        "category": None,
        "brand": None,
        "budget": None,
    }

    leaderboard = server.build_leaderboard(filters, limit=5)
    scores = [item["match_score"] for item in leaderboard]

    assert len(leaderboard) <= 5
    assert scores == sorted(scores, reverse=True)


def test_us05_recommendation_api_returns_required_fields(client):
    """TC-05.3: Recommendation JSON contains all required fields."""
    response = client.post(
        "/api/recommend",
        json={"category": "Laptops", "max_price": 1000},
    )
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert isinstance(data["data"], list)

    required_fields = {
        "product_id",
        "product_name",
        "name",
        "category",
        "brand",
        "price",
        "match_score",
        "reason",
    }

    for product in data["data"]:
        assert required_fields.issubset(product.keys())
        assert product["price"] <= 1000.0
