# 05 — HTTP methods: create, update, and delete

An HTTP method describes the kind of operation a client is asking an API to perform. This project uses `GET` to read products and adds `POST`, `PUT`, and `DELETE` routes in `main.py`.

## Validate request bodies with `ProductDTO`

The create and update routes accept a product in the request body. Their parameter is typed as `ProductDTO`, a Pydantic model defined in `dtos.py`:

```python
class ProductDTO(BaseModel):
    id: int
    title: str
    price: int = 0
    count: int = 0
```

The `id` and `title` fields are required. If `price` or `count` is omitted, its default is `0`. FastAPI uses this model to parse and validate the JSON body.

## POST — create a product

`POST /create_product` converts the validated model to a dictionary and appends it to the in-memory `products` list:

```python
@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status": "Product Created Successfully.", "data": products}
```

Example request body:

```json
{
  "id": 3,
  "title": "Keyboard",
  "price": 100,
  "count": 5
}
```

## PUT — replace a product

`PUT /update_product/{product_id}` takes the target ID from the URL and the replacement product from the request body. When it finds a matching product, it replaces that list entry with the full dictionary from `ProductDTO`.

For example, send a `PUT` request to `/update_product/1` with a JSON body containing `id`, `title`, and optionally `price` and `count`. This route replaces the whole product; it is not a partial update. The body’s `id` is not checked against the `product_id` in the URL, so keep them the same when using this API.

## DELETE — remove a product

`DELETE /delete_product/{product_id}` searches for the matching product and removes it from the list with `pop`. The response includes the removed product. If no product has that ID, the route returns an error dictionary.

## Try the routes

Start the app with `uv run uvicorn main:app --reload`, then open `http://127.0.0.1:8000/docs`. The interactive API page lets you select each route, enter a request body for POST or PUT, and try it.

## Current project limitations

The `products` list comes from `mockData.py` and is held in memory. Changes made by POST, PUT, or DELETE are temporary and are lost when the app restarts. Also, the not-found responses are currently ordinary dictionaries, so these routes do not set an HTTP error status for those cases.

## Check your understanding

Which method would you use to add a product, and which one would you use to remove a product by ID?
