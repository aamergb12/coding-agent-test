# coding-agent-test# Simple REST API

A basic REST API implementation using Flask.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:
```bash
python app.py
```

## API Endpoints

- GET /api/items - List all items
- GET /api/items/{id} - Get a specific item
- POST /api/items - Create a new item
- PUT /api/items/{id} - Update an item
- DELETE /api/items/{id} - Delete an item

## Example Usage

```bash
# Get all items
curl http://localhost:5000/api/items

# Create a new item
curl -X POST -H "Content-Type: application/json" -d '{"name": "Test Item", "description": "A test item"}' http://localhost:5000/api/items
```