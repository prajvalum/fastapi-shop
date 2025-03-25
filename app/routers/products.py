from fastapi import APIRouter
from app.models.product import Product
from app.db import products_db
from app.exceptions import product_already_exists
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
def list_products():
    return list(products_db.values())

@router.post("/", response_model=Product)
def create_product(product: Product):
    if product.id in products_db:
        product_already_exists()
    products_db[product.id] = product.model_dump()
    return product