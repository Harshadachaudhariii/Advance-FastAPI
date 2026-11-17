# 01 — Introduction to FastAPI

## What this project is learning

This repository is a starting point for learning how to build web APIs with FastAPI. An API lets another program send an HTTP request and receive a structured response, commonly JSON.

FastAPI is a Python framework for defining those API endpoints. It uses Python type hints to describe inputs and outputs, validates request data, and can generate interactive API documentation when an application is running.

## What the project contains today

- The project is named `advance-fastapi` and requires Python 3.11 or newer.
- FastAPI and Uvicorn are declared as dependencies in `pyproject.toml`.
- `main.py` creates a FastAPI application object named `app`.
- The application currently has two GET endpoints: `/` and `/contact`.

Uvicorn is an ASGI server commonly used to run the FastAPI application. It serves the app when started with the correct import path.

## What we will build toward

The lesson sequence progresses from a first endpoint and request parameters to data validation, database-backed operations, authentication, and background tasks. Later notes should describe those features only when they are present in the project, or clearly label them as the next lesson rather than existing behavior.

## Check your understanding

In your own words, what is the difference between the FastAPI framework and Uvicorn, and does this project have an HTTP endpoint yet?
