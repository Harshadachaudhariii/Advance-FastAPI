# 02 — Project setup

## Prerequisites

- Python 3.11 or newer (`pyproject.toml` sets `requires-python = ">=3.11"`).
- [uv](https://docs.astral.sh/uv/) to create the project environment and install the locked dependencies.

The project declares FastAPI and Uvicorn in `pyproject.toml`, and includes `uv.lock` to record resolved dependency versions.

## Install dependencies

From the repository root, run:

```powershell
uv sync
```

This creates or updates the project virtual environment and installs the dependencies from the project configuration and lock file.

## Run the current API

Start the development server from the repository root:

```powershell
uv run uvicorn main:app --reload
```

Here, `main` refers to `main.py`, `app` is the FastAPI instance defined in that module, and `--reload` restarts the server when source files change. Open these URLs in a browser:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/products`
- `http://127.0.0.1:8000/docs` for the interactive API documentation.

Running `uv run python main.py` is not how this API is served. The `if __name__ == "__main__"` block calls route functions directly and calls `get_one_porduct()` without its required `product_id`, so running the file directly currently raises an error. Start it with Uvicorn instead.

## Check your understanding

In `uv run uvicorn main:app --reload`, what do `main` and `app` refer to?
