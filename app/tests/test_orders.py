from fastapi.testclient import TestClient
from app.main import app
from app.db import products_db, orders_db

client = TestClient(app)

def test_create_order():
    # Ensure product exists before ordering
    products_db[1] = {
        "id": 1,
        "name": "Test Product",
        "description": "A sample product",
        "price": 99.99,
        "stock": 10
    }
    
    response = client.post("/orders/", json=[
        {"product_id": 1, "quantity": 2}
    ])
    assert response.status_code == 200
    assert response.json()["total_price"] == 199.98
    assert response.json()["status"] == "pending"

def test_order_insufficient_stock():
    response = client.post("/orders/", json=[
        {"product_id": 1, "quantity": 100}
    ])
    assert response.status_code == 400
    assert "Insufficient stock" in response.json()["detail"]

def test_order_invalid_product():
    response = client.post("/orders/", json=[
        {"product_id": 999, "quantity": 1}
    ])
    assert response.status_code == 404
    assert "Product 999 not found" in response.json()["detail"]