# 21 — User and task relationship

Each task is associated with a user through the `user_id` foreign key in [TaskModel](../../Task_Management_APP/src/tasks/models.py):

```python
user_id = Column(
    Integer,
    ForeignKey("user_table.id", ondelete="CASCADE"),
)
```

The key refers to `UserModel.id` in the `user_table` table. The foreign key lets the database enforce that a non-null task owner references a user. Its `ON DELETE CASCADE` option requests that the database remove a user's tasks when that user is deleted.

The current SQLAlchemy models do not declare ORM `relationship()` attributes such as `UserModel.tasks` or `TaskModel.user`. The application uses the foreign-key value directly instead: task creation sets `user_id` to the authenticated user's ID, and task queries filter on that column.

The Alembic revision in `migration/versions` adds this column and foreign key to an existing `user_tasks` table. The migration and model definitions should be kept aligned when the schema changes.

## Check your understanding

Does the current model define an ORM `relationship()` property, or does application code use the `user_id` foreign key directly?
