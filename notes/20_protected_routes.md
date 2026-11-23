# 20 — Protected routes

The task endpoints are protected by declaring the authentication helper as a dependency in [tasks/router.py](../../Task_Management_APP/src/tasks/router.py). For example:

```python
def get_all_tasks(
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticate),
):
    return controller.get_task(db, user)
```

Before calling the route function, FastAPI resolves `is_authenticate`. It returns a `UserModel` only when the request contains a token that decodes successfully and refers to an existing user. The route passes that user to its controller, which scopes task operations to the user's ID.

The create, list, fetch-by-ID, update, and delete task routes all use this dependency. The health routes are public. `/user/is_auth` is also not wired to this shared dependency; its controller reads and validates the request token directly.

Call a protected route with:

```http
Authorization: Bearer <token>
```

## Check your understanding

What does `Depends(is_authenticate)` provide to a task route when authentication succeeds?
