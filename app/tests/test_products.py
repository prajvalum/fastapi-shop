from fastapi.testclient import TestClient
from app.main import app
from app.db import products_db

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "id": 10,
        "name": "Test Product",
        "description": "A sample product",
        "price": 99.99,
        "stock": 10
    })
    assert response.status_code == 200
    assert response.json()["id"] == 10

def test_list_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)