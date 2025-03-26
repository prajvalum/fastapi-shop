from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.db import products_db
from app.exceptions import product_already_exists
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
def list_products():
    try:
        return list(products_db.values())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@router.post("/", response_model=Product)
def create_product(product: Product):
    try:
        if product.id in products_db:
            product_already_exists()
        
        products_db[product.id] = product.model_dump()
        return product
    
    except HTTPException as http_exc:
        raise http_exc  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
