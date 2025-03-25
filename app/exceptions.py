from fastapi import HTTPException

def product_not_found(product_id: int):
    raise HTTPException(status_code=404, detail=f"Product {product_id} not found")

def insufficient_stock(product_id: int):
    raise HTTPException(status_code=400, detail=f"Insufficient stock for product {product_id}")

def product_already_exists():
    raise HTTPException(status_code=400, detail="Product ID already exists")