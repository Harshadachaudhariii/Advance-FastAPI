# 14 — Best practices in the current app

This note reviews practices visible in the Task Management app. It describes the current code, including areas that would need more work before treating the API as production-ready.

## Practices already used

- **Separate concerns:** routers define HTTP endpoints, controllers contain database operations, DTOs define request/response shapes, and utility modules provide shared database and authentication helpers.
- **Use request and response schemas:** Pydantic schemas validate incoming JSON and prevent the password hash from appearing in user responses.
- **Hash passwords:** registration stores a hash created with `pwdlib` rather than the submitted password.
- **Scope tasks to their owner:** task queries and mutations use the authenticated user's ID.
- **Manage database sessions:** `get_db()` yields a session and closes it in a `finally` block.
- **Keep configuration outside source:** database and JWT settings are read through Pydantic Settings from `.env`; secret values should not be committed.

## Current limitations to keep in mind

- `Base.metadata.create_all()` creates missing tables but does not migrate existing schemas. Alembic is configured and should be used carefully when schema changes are needed.
- JWT authentication logic exists in both [helpers.py](../../Task_Management_APP/src/utils/helpers.py) and [controller.py](../../Task_Management_APP/src/user/controller.py). Keeping one shared implementation would avoid behavior drifting between task routes and `/user/is_auth`.
- DTOs mostly use basic types; for example, the email field is a `str`, and the schemas do not add length constraints or custom validation.
- The email task runs in the application process. It is not a durable queue with retries if the process stops or delivery fails.
- The application has no automated test files in the current source tree.

## Check your understanding

Name one existing practice that protects user data and one limitation that would matter when deploying the app.
