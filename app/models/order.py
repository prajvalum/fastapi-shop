from pydantic import BaseModel
from typing import List
from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    id: int
    products: List[OrderItem]
    total_price: float
    status: OrderStatus