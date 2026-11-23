# 22 — Keeping tasks scoped to users

The app uses the authenticated user's ID to keep task operations within that user's account. The task routes obtain the user from `is_authenticate()` and pass it to the controller.

- **Create:** `create_task()` assigns `user_id=user.id` to the new `TaskModel`.
- **List:** `get_task()` filters rows with `TaskModel.user_id == user.id`.
- **Fetch:** `get_one_task()` filters by both task ID and user ID.
- **Update and delete:** the controller loads the task, then compares `task.user_id` with `user.id` before changing or removing it.

This is important even when task IDs are difficult to guess: every operation that accesses an existing task must enforce ownership on the server. The request body does not let the client choose an owner ID when creating a task.

The current update and delete controllers first retrieve a task by ID and then perform the ownership check. A missing task returns `404`; an existing task owned by someone else returns `401`.

## Check your understanding

Why should the API derive a new task's owner from the authenticated user instead of trusting an owner ID in the request body?
