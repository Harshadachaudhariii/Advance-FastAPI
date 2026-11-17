# 04 — Path and query parameters

The current app uses both path and query parameters. Path parameters are part of the URL path; query parameters appear after `?`.

## Path parameters

The product route contains a placeholder in its path:

```python
@app.get("/product/{product_id}")
def get_one_porduct(product_id: int):
    for oneproduct in products:
        if oneproduct.get("id") == product_id:
            return oneproduct
    return {"error": "Product not found for this ID."}
```

For a request to `/product/1`, FastAPI takes `1` from the URL and passes it as `product_id`. The `int` type annotation tells FastAPI to convert and validate the value as an integer. A value that is not an integer is rejected during request validation.

The function searches the `products` list imported from `mockData.py`. It returns the matching item or an error dictionary if there is no match.

## Query parameters with type hints

Query parameters follow `?` in a URL and are separated by `&`. For example:

```text
/greet?name=Alice&age=25
```

The typed handler in `main.py` reads these values as function parameters:

```python
@app.get("/greet")
def greet_user(name: str, age: int):
    return {
        "greet": f"Hello {name}, How are you? and you are {age} years old."
    }
```

FastAPI gets `name` and `age` from the query string, converts `age` to an integer, and validates both. With no default values, both parameters are required.

## Reading the query string from `Request`

The file also imports `Request` and defines another handler that reads the query values from the request:

```python
@app.get("/greet")
def greet_user2(request: Request):
    query_params = dict(request.query_params)
    return {
        "greet": f"Hello {query_params.get('name')}, How are you? "
                 f"and you are {query_params.get('age')} years old."
    }
```

`request.query_params` provides the query values as strings. This approach gives direct access to the request but does not automatically validate and convert `age` to an integer as the typed-parameter approach does.

## Fix the duplicate route

Both `greet_user` and `greet_user2` are registered for `GET /greet`. These are alternative implementations, not two distinct endpoints. Keep only one handler for a given HTTP method and path; duplicate routes can lead to confusing request behavior and duplicate-operation warnings in the generated API documentation.

## Try it

Start the app with `uv run uvicorn main:app --reload`, then try:

```text
http://127.0.0.1:8000/product/1
http://127.0.0.1:8000/greet?name=Alice&age=25
```

## Check your understanding

What is the difference between `product_id` in `/product/1` and `name` in `/greet?name=Alice&age=25`?
