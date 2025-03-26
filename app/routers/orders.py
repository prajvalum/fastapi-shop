from fastapi import APIRouter, HTTPException
from app.models.order import Order, OrderItem
from app.db import orders_db, products_db
from app.exceptions import product_not_found, insufficient_stock
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=Order)
def create_order(order_items: List[OrderItem]):
    try:
        if not order_items:
            raise HTTPException(status_code=400, detail="Order must contain at least one product")

        total_price = 0.0
        order_id = len(orders_db) + 1

        for item in order_items:
            product = products_db.get(item.product_id)
            if not product:
                product_not_found(item.product_id)
            if product["stock"] < item.quantity:
                insufficient_stock(item.product_id)
                
            total_price += product["price"] * item.quantity
            product["stock"] -= item.quantity
        
        order = Order(id=order_id, products=order_items, total_price=total_price, status="pending")
        orders_db[order_id] = order.model_dump()
        return order
    
    except HTTPException as http_exc:
        raise http_exc 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
