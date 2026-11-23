# 13 — Updating and deleting tasks

The Task Management app exposes full task update and deletion routes. Both require a valid authenticated user and a database session.

## Update a task

`PUT /tasks/update_task/{task_id}` accepts the same `TaskSchema` body used to create a task. The controller loads the row by ID, returns `404` if it does not exist, and checks that its `user_id` matches the authenticated user. A different owner receives `401 Unauthorized`.

For an authorized task, the controller copies every schema field onto the model, commits the transaction, refreshes the model, and returns it:

```python
data = body.model_dump()
for field, value in data.items():
    setattr(task, field, value)

db.commit()
db.refresh(task)
```

The route declares `201 Created` as its success status, which is the current implementation even though the operation updates an existing resource.

## Delete a task

`DELETE /tasks/delete_task/{task_id}` uses the same lookup and ownership checks. If authorized, it calls `db.delete(task)`, commits, and returns no response body with `204 No Content`.

Both operations expect the login token in the authorization header. A task belonging to another user cannot be updated or deleted through these routes.

## Check your understanding

Which two checks does the controller perform before changing or deleting a task?
