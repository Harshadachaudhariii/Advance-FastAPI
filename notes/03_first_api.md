# 03 — Your first FastAPI endpoints

## The application object

In `main.py`, the app is created with:

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()` creates the application. Uvicorn imports the `app` object from the `main` module to serve it.

## Registering endpoints

The project currently defines two GET endpoints:

```python
@app.get("/")
def home():
    return "Welcome to FastAPI Series!"


@app.get("/contact")
def contact():
    return "Contact with us any time."
```

`@app.get("/")` tells FastAPI to call `home()` when a client sends an HTTP GET request to the root path `/`. The `/contact` route works the same way for that path. The returned strings become the response bodies.

| Method | Path | Response body |
|---|---|---|
| GET | `/` | `Welcome to FastAPI Series!` |
| GET | `/contact` | `Contact with us any time.` |

You can inspect and try the endpoints at `http://127.0.0.1:8000/docs` after starting the server.

## Start the server

From the project directory, run:

```powershell
uv run uvicorn main:app --reload
```

`main:app` means “import the `app` object from `main.py`.” The `--reload` option is useful while developing because the server restarts after source changes.

## The `main()` function

The current file also has a `main()` function that directly calls `home()`. That call is an ordinary Python function call; it does not send an HTTP request or start the API server. Uvicorn serves the routes through the `app` object instead.

## Check your understanding

Which function handles a GET request to `/contact`, and what does `main:app` tell Uvicorn to load?
