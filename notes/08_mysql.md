# 08 — MySQL database connection

The Task Management app uses MySQL through SQLAlchemy and the PyMySQL driver. This note follows the current database code in the sibling `Task_Management_APP` project; despite this file's existing name, the database lesson is MySQL, not PostgreSQL.

## Configure the connection

The app reads `DATABASE_URL` from its `.env` file using Pydantic Settings in [settings.py](../../Task_Management_APP/src/utils/settings.py). The actual URL contains credentials, so do not print or commit it. Its general SQLAlchemy format for this driver is:

```text
mysql+pymysql://<user>:<password>@<host>:<port>/<database>
```

In [db.py](../../Task_Management_APP/src/utils/db.py), `create_engine()` receives that setting. The project includes `pymysql` and `sqlalchemy` in [pyproject.toml](../../Task_Management_APP/pyproject.toml). The same module defines a session factory and `get_db()`, which provides a session to a request and closes it afterward.

## Check the connection on startup

The lifespan handler in [main.py](../../Task_Management_APP/main.py) opens a connection and runs a simple query:

```python
with engine.connect() as connection:
    connection.execute(text("SELECT 1"))
```

If that succeeds, the app prints its success message and then calls `Base.metadata.create_all(bind=engine)`. If connecting raises an exception, startup fails. The `GET /test-db` endpoint also runs `SELECT 1`, using a session supplied by `get_db()`.

## Tables and schema changes

The current app defines mapped SQLAlchemy models for users and tasks, so `create_all()` can create their tables when they are missing. It does not update an existing table when a model changes. Alembic is also configured for migrations; review the migration history before applying a migration to a database that already contains data.

## Check your understanding

Which file creates the SQLAlchemy engine, and where does its `DATABASE_URL` setting come from?
