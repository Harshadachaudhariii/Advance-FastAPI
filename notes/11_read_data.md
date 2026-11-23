# 11 — Reading task data

The app lists tasks with `GET /tasks/all_tasks`. The route in [router.py](../../Task_Management_APP/src/tasks/router.py) requires both a database session and the authenticated user, then delegates to the task controller.

The controller queries `TaskModel` rows whose `user_id` matches the current user's ID:

```python
tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
return tasks
```

The route declares a list of `TaskResponseSchema` objects as its response model. FastAPI serializes each returned model to JSON. If the user has no tasks, the query returns an empty list.

To try it, send the login token in the authorization header:

```bash
curl http://127.0.0.1:8000/tasks/all_tasks \
  -H "Authorization: Bearer <token>"
```

The list is scoped to the logged-in user; this endpoint does not return every task in the database.

## Check your understanding

Which task column does the list query use to filter records for the current user?
