# 16 — User registration

The registration endpoint is `POST /user/register`, defined in [router.py](../../Task_Management_APP/src/user/router.py). It accepts a `UserSchema` containing `name`, `username`, `hash_password`, and `email`.

The async `register()` controller in [controller.py](../../Task_Management_APP/src/user/controller.py) performs these steps:

1. Look up an existing user with the same username; return `400 Bad Request` if found.
2. Look up an existing user with the same email; return `400 Bad Request` if found.
3. Hash the supplied password with `pwdlib`.
4. Create a `UserModel`, add it to the database session, commit, and refresh it.
5. Schedule the confirmation email as a background task.

The route returns `201 Created` and uses `UserResponseSchema`, which includes the user's ID, name, username, and email, but not the password hash.

Example request:

```json
{
  "name": "Alex Morgan",
  "username": "alex",
  "hash_password": "choose-a-password",
  "email": "alex@example.com"
}
```

The current duplicate checks are performed in application code. The user model does not declare unique constraints for username or email.

## Check your understanding

Why does the registration response use a separate response schema instead of returning every user model column?
