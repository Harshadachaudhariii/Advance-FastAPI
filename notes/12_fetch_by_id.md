# 12 — Fetching a task by ID

The app retrieves one task through `GET /tasks/one_task/{task_id}`. FastAPI reads `task_id` from the path and validates it as an integer. The route also injects the database session and authenticated user.

In [controller.py](../../Task_Management_APP/src/tasks/controller.py), the query filters on both the requested task ID and the current user's ID:

```python
one_task = (
    db.query(TaskModel)
    .filter(TaskModel.id == task_id, TaskModel.user_id == user.id)
    .first()
)
if not one_task:
    raise HTTPException(404, detail="Task ID is Incorrect")
```

If a matching task is found, the route returns it using `TaskResponseSchema`. If it is missing or belongs to a different user, the query finds no row and the API returns `404 Not Found`.

Example:

```bash
curl http://127.0.0.1:8000/tasks/one_task/1 \
  -H "Authorization: Bearer <token>"
```

## Check your understanding

Why does this query include `user.id` as well as `task_id`?
