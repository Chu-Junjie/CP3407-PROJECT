import sqlite3
from pathlib import Path

import pytest

import server


@pytest.fixture(autouse=True)
def isolated_database(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    source = tmp_path / "source.db"
    connection = sqlite3.connect(source)
    connection.execute(
        "CREATE TABLE products (ProductID INTEGER, ProductCategory TEXT, "
        "ProductBrand TEXT, ProductPrice REAL, CustomerAge INTEGER, "
        "CustomerGender TEXT, PurchaseFrequency INTEGER, "
        "CustomerSatisfaction INTEGER, PurchaseIntent INTEGER)"
    )
    categories = ["Laptops", "Smartphones", "Tablets", "Headphones", "Smart Watches"]
    brands = ["Apple", "Samsung", "HP", "Sony", "Other Brands"]
    rows = [
        (index, categories[index % 5], brands[index % 5], 100 + index * 10,
         20 + index % 30, "Other", index % 10, 1 + index % 5, index % 2)
        for index in range(1, 61)
    ]
    connection.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)
    connection.execute(
        "CREATE TABLE product_specs (ProductID INTEGER PRIMARY KEY, ProductName TEXT, "
        "CPU TEXT, GPU TEXT, RAM TEXT, Storage TEXT, ScreenSize TEXT, BatteryLife TEXT, "
        "Weight TEXT, UseCase TEXT, PurchaseURL TEXT, DataSource TEXT, LastUpdated TEXT)"
    )
    spec_rows = [
        (index, f"Public Dataset Product {index}", "Recorded CPU", "Recorded GPU", "8GB", "256GB",
         "14 inch", "10 hours", "1.4 kg", "study office fitness travel",
         "https://example.com/dataset", "test-public-dataset", "2026-08-05T00:00:00+00:00")
        for index in range(1, 41)
    ]
    connection.executemany("INSERT INTO product_specs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", spec_rows)
    connection.commit()
    connection.close()

    monkeypatch.setattr(server, "SQLITE_SEED_PATH", source)
    server.configure_database(f"sqlite:///{tmp_path / 'app.db'}")
    server.app.config.update(TESTING=True)
    yield
    server.engine.dispose()


@pytest.fixture
def client():
    with server.app.test_client() as test_client:
        yield test_client


def register(client, username="student"):
    response = client.post("/api/auth/register", json={
        "username": username,
        "email": f"{username}@example.com",
        "password": "Password123!",
    })
    assert response.status_code == 201
    return response.get_json()["token"]


def auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_database_setup_creates_real_tables_and_40_catalogue_records():
    counts = server.setup_database()
    assert counts == {
        "products": 60,
        "product_specs": 40,
        "users": 0,
        "favorites": 0,
        "search_history": 0,
        "feedback": 0,
    }
    assert server.setup_database()["product_specs"] == 40


def test_health_reports_database_counts(client):
    response = client.get("/api/health")
    body = response.get_json()
    assert response.status_code == 200
    assert body["database"] == "sqlite"
    assert body["joined_recommendation_candidates"] == 40


def test_budget_and_category_are_parsed():
    assert server.parse_budget_from_text("laptop under $1,500") == 1500
    assert server.infer_category_from_text("portable university laptop") == "Laptops"


def test_recommendation_is_paginated_not_limited_to_five(client):
    response = client.post("/api/recommend", json={"query": "under $1000", "per_page": 20})
    body = response.get_json()
    assert response.status_code == 200
    assert body["count"] == 20
    assert body["total_candidates"] == 40
    assert body["total_pages"] == 2
    assert len(body["top_recommendations"]) == 5


def test_second_recommendation_page_is_available(client):
    body = client.post("/api/recommend", json={"query": "under $1000", "page": 2, "per_page": 20}).get_json()
    assert body["page"] == 2
    assert len(body["data"]) == 20


def test_registration_login_and_me(client):
    token = register(client)
    assert client.get("/api/auth/me", headers=auth(token)).status_code == 200
    login = client.post("/api/auth/login", json={"identifier": "student@example.com", "password": "Password123!"})
    assert login.status_code == 200
    assert login.get_json()["user"]["username"] == "student"


def test_search_history_is_private_and_persistent(client):
    token = register(client)
    search = client.post("/api/recommend", json={"query": "phone under $700"}, headers=auth(token)).get_json()
    history_id = search["history_id"]
    assert history_id
    assert client.get("/api/history").status_code == 401
    listing = client.get("/api/history", headers=auth(token)).get_json()
    assert listing["total"] == 1
    detail = client.get(f"/api/history/{history_id}", headers=auth(token)).get_json()
    assert detail["history"]["query_text"] == "phone under $700"
    assert detail["data"]


def test_history_can_be_deleted(client):
    token = register(client)
    history_id = client.post("/api/recommend", json={"query": "tablet"}, headers=auth(token)).get_json()["history_id"]
    assert client.delete(f"/api/history/{history_id}", headers=auth(token)).status_code == 200
    assert client.get("/api/history", headers=auth(token)).get_json()["total"] == 0


def test_feedback_is_stored_and_summarised(client):
    server.setup_database()
    result = client.post("/api/feedback", json={"vote": "up", "query": "laptop"})
    assert result.status_code == 201
    summary = client.get("/api/feedback").get_json()["data"]
    assert summary == {"up": 1, "down": 0, "total": 1}


def test_compare_requires_two_or_three_products(client):
    server.setup_database()
    assert client.post("/api/compare", json={"product_ids": [1]}).status_code == 400
    response = client.post("/api/compare", json={"product_ids": [1, 2]})
    assert response.status_code == 200
    assert response.get_json()["count"] == 2


def test_favorites_are_private_and_persistent(client):
    token = register(client)
    headers = auth(token)
    assert client.post("/api/favorites", json={"product_id": 1}, headers=headers).status_code == 201
    assert client.post("/api/favorites", json={"product_id": 6}, headers=headers).status_code == 201
    assert client.get("/api/favorites").status_code == 401
    listing = client.get("/api/favorites", headers=headers).get_json()
    assert listing["count"] == 2
    assert {item["product_id"] for item in listing["data"]} == {1, 6}
    assert client.delete("/api/favorites/1", headers=headers).status_code == 200
    assert client.get("/api/favorites", headers=headers).get_json()["count"] == 1


def test_favorite_comparison_requires_same_category(client):
    token = register(client)
    headers = auth(token)
    for product_id in (1, 6, 2):
        assert client.post("/api/favorites", json={"product_id": product_id}, headers=headers).status_code == 201
    same = client.post("/api/favorites/compare", json={"product_ids": [1, 6]}, headers=headers)
    assert same.status_code == 200
    assert same.get_json()["category"] == "Smartphones"
    mixed = client.post("/api/favorites/compare", json={"product_ids": [1, 2]}, headers=headers)
    assert mixed.status_code == 400
    assert "same category" in mixed.get_json()["message"]
