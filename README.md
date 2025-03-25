
### Prerequisites
- Python 3.8
- Docker

### Installation
1. Clone the repository:
```sh
git clone https://github.com/prajvalum/fastapi-shop.git
cd fastapi-shop
```

2. Create and activate a virtual environment:
```sh
python3.8 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

### Running the Server
```sh
uvicorn app.main:app --reload
```

### Running Tests
```sh
pytest app/tests/
```

## Docker Deployment
### Build the Image
```sh
docker build -t fastapi-shop .
```

### Run the Container
```sh
docker run -p 8000:8000 fastapi-shop
```

## API Endpoints
### Products
- `GET /products/` - List all products
- `POST /products/` - Add a new product

### Orders
- `POST /orders/` - Place an order

For detailed API documentation, visit `http://localhost:8000/docs` after starting the server.
