# 06 — Pydantic request models

Pydantic models describe the shape and types of data an API expects. This project defines `ProductDTO` in `dtos.py` and uses it for the create and update request bodies in `main.py`.

## Define the product fields

```python
from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    title: str
    price: int = 0
    count: int = 0
```

`id` and `title` are required. `price` and `count` are optional because they have default values; if omitted, each is set to `0`. The type annotations tell Pydantic what values to validate and convert.

## Use the model in an endpoint

The create and update handlers accept `ProductDTO` as a parameter:

```python
@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status": "Product Created Successfully.", "data": products}
```

FastAPI reads the JSON request body, validates it against `ProductDTO`, and passes a model instance to the handler. If required fields are missing or values cannot be validated, FastAPI returns a request-validation error instead of calling the handler.

`model_dump()` converts the validated model to a regular Python dictionary. The current handlers use that dictionary to append or replace items in the `products` list. The data is still only in memory; Pydantic validates the request but does not save it to a database.

## Try it

Start the app with `uv run uvicorn main:app --reload`, open `http://127.0.0.1:8000/docs`, and try `POST /create_product` with this body:

```json
{
  "id": 3,
  "title": "Keyboard",
  "price": 100
}
```

Notice that `count` can be omitted because it defaults to `0`. Then remove `title` and submit again to see request validation reject the body.

## Check your understanding

Which fields in `ProductDTO` can be omitted, and what values do they receive?
