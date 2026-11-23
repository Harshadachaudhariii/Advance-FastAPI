# 10 — Creating task data

The Task Management app creates tasks through the authenticated `POST /tasks/create` endpoint. The route is defined in [router.py](../../Task_Management_APP/src/tasks/router.py), while the database work is in [controller.py](../../Task_Management_APP/src/tasks/controller.py).

## Request data

The route accepts a `TaskSchema` JSON body:

```json
{
  "title": "Prepare project notes",
  "description": "Review the API documentation",
  "is_completed": false
}
```

In [dtos.py](../../Task_Management_APP/src/tasks/dtos.py), `title` and `description` are required strings. `is_completed` is a Boolean that defaults to `False` when omitted. Pydantic validates the incoming values before the route calls the controller.

## Save the task

The route also gets a SQLAlchemy session from `get_db()` and the current user from `is_authenticate`. The controller converts the input schema to a dictionary, creates a `TaskModel`, and sets `user_id` from the authenticated user rather than accepting an owner ID from the request body:

```python
data = body.model_dump()
new_task = TaskModel(
    title=data["title"],
    description=data["description"],
    is_completed=data["is_completed"],
    user_id=user.id,
)

db.add(new_task)
db.commit()
db.refresh(new_task)
```

`add()` stages the new row in the session, `commit()` saves the transaction, and `refresh()` reads the generated database values back onto the model. The route returns the new task using `TaskResponseSchema` and the `201 Created` status.

## Try it

Log in to get a token, then send a create request with that token:

```bash
curl -X POST http://127.0.0.1:8000/tasks/create \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title":"Prepare project notes","description":"Review the API documentation","is_completed":false}'
```

The response contains the task ID assigned by the database, its fields, and the authenticated user's ID.

## Check your understanding

Where does the create-task controller get the new task's `user_id` from?
