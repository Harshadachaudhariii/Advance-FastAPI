# 03 — Your first FastAPI endpoints

## Create the application

The project creates a FastAPI application in `main.py`:

```python
from fastapi import FastAPI
from mockData import products

app = FastAPI()
```

`app` is the application object that Uvicorn serves. The `products` list is imported from `mockData.py`.

## Add routes

A route decorator connects an HTTP method and URL path to a Python function:

```python
@app.get("/")
def home():
    return "Welcome to FastAPI Series!"
```

When a client sends a GET request to `/`, FastAPI calls `home()` and returns its result.

The project also has a collection endpoint:

```python
@app.get("/products")
def get_products():
    return products
```

It returns the product list, whose sample entries are defined in `mockData.py`. The project has additional routes for individual products and greetings; their path and query parameters are covered in [04_path_query_params.md](./04_path_query_params.md).

## Current route overview

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Returns a welcome message. |
| GET | `/products` | Returns the product list. |
| GET | `/product/{product_id}` | Returns a product matching the path value. |
| GET | `/greet` | Greeting endpoint; parameter details are in the next note. |

The `/greet` route is currently declared twice. The duplicate-route issue is explained in the next note.

## Run the API

From the project directory, start the development server:

```powershell
uv run uvicorn main:app --reload
```

`main:app` means “load the `app` object from `main.py`.” Then visit `http://127.0.0.1:8000/docs` to explore the routes in FastAPI's interactive documentation.

Running `uv run python main.py` does not start the API. The current `if __name__ == "__main__"` block calls route functions directly and calls `get_one_porduct()` without its required argument, so running the file directly currently raises an error.

## Check your understanding

What does `@app.get("/products")` connect, and which function handles that route?
