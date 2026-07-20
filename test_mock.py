"""Mock-object tests for Practical 8, Task 7.

These tests use Python's built-in unittest.mock framework to isolate
the Flask routes, database layer, CSV loader, and recommendation engine.
"""

from unittest.mock import MagicMock, patch

import server


REQUIRED_COLUMNS = [
    "ProductID",
    "ProductCategory",
    "ProductBrand",
    "ProductPrice",
    "CustomerAge",
    "CustomerGender",
    "PurchaseFrequency",
    "CustomerSatisfaction",
    "PurchaseIntent",
]


def create_mock_connection() -> MagicMock:
    """Create a context-manager-compatible mock SQLite connection."""
    connection = MagicMock()
    connection.__enter__.return_value = connection
    connection.__exit__.return_value = False
    return connection


def test_mock_database_setup_imports_csv_when_table_is_missing():
    """MOCK-01: Simulate CSV import without using the real database."""
    connection = create_mock_connection()

    # Simulate that the products table does not exist.
    connection.execute.return_value.fetchone.return_value = [0]

    dataframe = MagicMock()
    dataframe.columns = REQUIRED_COLUMNS
    dataframe.__len__.return_value = 3

    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("server.get_connection", return_value=connection),
        patch("server.pd.read_csv", return_value=dataframe) as mock_read_csv,
    ):
        row_count = server.setup_database()

    assert row_count == 3
    mock_read_csv.assert_called_once_with(server.CSV_PATH)
    dataframe.to_sql.assert_called_once_with(
        server.TABLE_NAME,
        connection,
        if_exists="replace",
        index=False,
    )
    connection.commit.assert_called_once()


def test_mock_health_endpoint_without_real_database():
    """MOCK-02: Replace database setup with a controlled row count."""
    with patch("server.setup_database", return_value=42) as mock_setup:
        with server.app.test_client() as client:
            response = client.get("/api/health")

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["records"] == 42
    assert data["table"] == server.TABLE_NAME
    mock_setup.assert_called_once_with()


def test_mock_recommend_endpoint_without_running_real_engine():
    """MOCK-03: Isolate the API route from the real recommendation engine."""
    fake_filters = {
        "query": "laptop under $1000 no Apple",
        "category": "Laptops",
        "brand": None,
        "budget": 1000.0,
        "exclusions": ["apple"],
    }

    fake_leaderboard = [
        {
            "product_id": 2,
            "product_name": "HP Laptops #2",
            "name": "HP Laptops #2",
            "category": "Laptops",
            "brand": "HP",
            "price": 700.0,
            "match_score": 66,
            "reason": "matches category: Laptops; within budget $1000",
        }
    ]

    with (
        patch("server.read_request_filters", return_value=fake_filters)
        as mock_read_filters,
        patch(
            "server.build_leaderboard",
            return_value=fake_leaderboard,
        ) as mock_build_leaderboard,
    ):
        with server.app.test_client() as client:
            response = client.post(
                "/api/recommend",
                json={"query": "this request is replaced by mocks"},
            )

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["filters"] == fake_filters
    assert data["data"] == fake_leaderboard

    mock_read_filters.assert_called_once_with()
    mock_build_leaderboard.assert_called_once_with(
        fake_filters,
        limit=5,
    )


def test_mock_database_query_contains_exclusion_filter():
    """MOCK-04: Verify SQL exclusion logic without opening SQLite."""
    connection = create_mock_connection()
    connection.execute.return_value.fetchall.return_value = []

    filters = {
        "query": "no Apple",
        "category": None,
        "brand": None,
        "budget": None,
        "exclusions": ["apple"],
    }

    with patch("server.get_connection", return_value=connection):
        products = server.fetch_candidate_products(filters)

    assert products == []

    sql, params = connection.execute.call_args.args

    assert "LOWER(TRIM(ProductBrand)) != ?" in sql
    assert params == ["apple"]


def test_mock_leaderboard_uses_controlled_candidate_products():
    """MOCK-05: Test ranking with mock candidates instead of database rows."""
    filters = {
        "query": "",
        "category": "Laptops",
        "brand": "Apple",
        "budget": 1000.0,
        "exclusions": [],
    }

    fake_candidates = [
        {
            "ProductID": 1,
            "ProductCategory": "Laptops",
            "ProductBrand": "Apple",
            "ProductPrice": 900,
            "CustomerAge": 22,
            "CustomerGender": "Female",
            "PurchaseFrequency": 8,
            "CustomerSatisfaction": 5,
            "PurchaseIntent": 1,
        },
        {
            "ProductID": 2,
            "ProductCategory": "Laptops",
            "ProductBrand": "HP",
            "ProductPrice": 700,
            "CustomerAge": 30,
            "CustomerGender": "Male",
            "PurchaseFrequency": 3,
            "CustomerSatisfaction": 2,
            "PurchaseIntent": 0,
        },
    ]

    with (
        patch("server.setup_database", return_value=2) as mock_setup,
        patch(
            "server.fetch_candidate_products",
            return_value=fake_candidates,
        ) as mock_fetch,
    ):
        leaderboard = server.build_leaderboard(filters, limit=1)

    assert len(leaderboard) == 1
    assert leaderboard[0]["brand"] == "Apple"
    assert leaderboard[0]["match_score"] > 0

    mock_setup.assert_called_once_with()
    mock_fetch.assert_called_once_with(filters)


def test_mock_missing_csv_error_response():
    """MOCK-06: Simulate a missing CSV file and verify the API error."""
    error = FileNotFoundError(
        "Missing dataset: US-02 Database Setup & Import.csv"
    )

    with patch("server.setup_database", side_effect=error):
        with server.app.test_client() as client:
            response = client.get("/api/health")

    data = response.get_json()

    assert response.status_code == 500
    assert data["status"] == "error"
    assert "Missing dataset" in data["message"]
