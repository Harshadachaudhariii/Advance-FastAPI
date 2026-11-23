# 17 — Request validation

FastAPI uses the Pydantic models in the app's DTO modules to validate JSON request bodies before calling route handlers.

In [user/dtos.py](../../Task_Management_APP/src/user/dtos.py), `UserSchema` requires string values for `name`, `username`, `hash_password`, and `email`. `LoginSchema` requires a username and password. In [tasks/dtos.py](../../Task_Management_APP/src/tasks/dtos.py), `TaskSchema` requires string `title` and `description` values and defines `is_completed` as a Boolean defaulting to `False`.

For example, the task body can omit the completion flag:

```json
{
  "title": "Prepare project notes",
  "description": "Review the API documentation"
}
```

Pydantic supplies `false` for `is_completed`. Missing required fields or values that cannot be parsed as the declared types are rejected by FastAPI before the controller runs. Successful validation does not guarantee every business rule: duplicate username/email checks happen in the registration controller.

## Validation not currently implemented

The email fields are declared as `str`, not `EmailStr`, so the DTO does not check email-address formatting. The schemas also do not define additional length limits or custom validators. The database columns impose their own length definitions, but adding explicit request constraints would make the API's validation rules clearer.

## Check your understanding

Which field in `TaskSchema` has a default, and what value does it use?
