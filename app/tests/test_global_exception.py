from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import HTTPException
from app.main import app
from app.routers.products import list_products

client = TestClient(app)

def test_http_exception_handler():
    response = client.get("/non-existing-endpoint")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
