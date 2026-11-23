# 09 — SQLAlchemy models

SQLAlchemy models describe database tables in Python. In the current Task Management app, the models are defined in the sibling `Task_Management_APP` project and inherit from the shared `Base` in [db.py](../../Task_Management_APP/src/utils/db.py).

## User and task tables

[UserModel](../../Task_Management_APP/src/user/models.py) maps to the `user_table` table. It defines an integer primary key and columns for a name, username, password hash, and email. The password column is named `hash_password`; the registration controller hashes the supplied password before storing it.

[TaskModel](../../Task_Management_APP/src/tasks/models.py) maps to `user_tasks`. Its columns include:

- `id`: integer primary key.
- `title` and `description`: strings with a maximum length of 255.
- `is_completed`: Boolean with a default of `False`.
- `user_id`: integer foreign key referencing `user_table.id`, with `ON DELETE CASCADE`.

The models use SQLAlchemy's `Column` declarations. For example, the task owner is represented by a foreign key:

```python
user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))
```

This foreign key records which user owns a task and lets the database enforce the reference. The current models do not define SQLAlchemy `relationship()` attributes; application code filters tasks by `user_id` instead.

## Models are not request schemas

The SQLAlchemy models describe stored database rows. The Pydantic schemas in [task dtos](../../Task_Management_APP/src/tasks/dtos.py) and [user dtos](../../Task_Management_APP/src/user/dtos.py) describe API input and output. For example, `TaskSchema` accepts a title, description, and completion flag; the controller then creates a `TaskModel` and assigns the authenticated user's ID.

## How tables are created

[main.py](../../Task_Management_APP/main.py) imports the routers, which import the model classes. During application startup it calls `Base.metadata.create_all(bind=engine)`. That creates missing tables for models registered on the shared `Base`; it does not modify existing tables to match later model changes. The project also has an Alembic migration for adding the task owner foreign key.

## Check your understanding

Which field in `TaskModel` connects each task row to its owner, and which class defines the user table?
