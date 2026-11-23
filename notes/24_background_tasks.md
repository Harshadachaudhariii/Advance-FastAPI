# 24 — Background tasks

The registration endpoint uses FastAPI's `BackgroundTasks` to schedule confirmation email after the user has been saved. The route in [user/router.py](../../Task_Management_APP/src/user/router.py) receives the background-task collector and passes it into the async registration controller.

In [controller.py](../../Task_Management_APP/src/user/controller.py), the controller checks for duplicate username and email, hashes the password, creates the user, commits the database session, and refreshes the new row. It then schedules the email:

```python
bg_task.add_task(send_email, [new_user.email])
```

FastAPI runs the scheduled task after sending the HTTP response, so the request handler does not wait for SMTP delivery to finish. Registration still returns the user response with `201 Created`.

FastAPI background tasks run as part of the application process. The current implementation does not provide a persistent job queue, automatic retries, or recovery if the process stops while a task is pending. For work that must be durable or retried, a dedicated task-queue system would be needed.

## Check your understanding

At what point does FastAPI run the registration email task relative to sending the HTTP response?
