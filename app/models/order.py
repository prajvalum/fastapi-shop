from pydantic import BaseModel
from typing import List
from app.models.product import Product

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    id: int
    products: List[OrderItem]
    total_price: float
    status: str  # pending, completed