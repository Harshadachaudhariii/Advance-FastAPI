# 07 — Project structure

This project currently uses a small, flat layout. Its API routes, request model, and sample data are in separate files at the project root:

```text
advance-fastapi/
├── main.py
├── dtos.py
├── mockData.py
├── pyproject.toml
├── uv.lock
└── notes/
```

## What each file does

- `main.py` creates the FastAPI app and defines the route handlers.
- `dtos.py` defines `ProductDTO`, the Pydantic model used to validate create and update request bodies.
- `mockData.py` contains the sample `products` list imported by `main.py`.
- `pyproject.toml` declares the project metadata, Python requirement, and dependencies. `uv.lock` records resolved dependency versions.
- `notes/` contains the learning notes for this project.

Because `main.py`, `dtos.py`, and `mockData.py` are all at the project root, `main.py` imports them directly with `from dtos import ProductDTO` and `from mockData import products`.

## What is not separated yet

There are no route modules, database models, service layer, or database package in this project yet. All endpoint functions remain in `main.py`, and the sample product data remains in `mockData.py`. This note describes the current layout; a larger structure should be introduced when the project actually adds those components.

## Check your understanding

Which file currently defines the API routes, and which file holds the sample product data?
