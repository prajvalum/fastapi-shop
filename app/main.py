from fastapi import FastAPI, Request, HTTPException
import uvicorn
from app.routers import products, orders
from fastapi.responses import JSONResponse

app = FastAPI(title="E-Commerce API", description="A simple e-commerce backend with FastAPI")

# Global exception handler
@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# Register API routers
app.include_router(products.router)
app.include_router(orders.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)