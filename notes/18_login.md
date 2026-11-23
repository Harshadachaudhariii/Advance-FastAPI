# 18 — Logging in

The app's login endpoint is `POST /user/login`. It accepts a `LoginSchema` with `username` and `hash_password`, then calls `user_login()` in [controller.py](../../Task_Management_APP/src/user/controller.py).

The controller looks up the account by username. If it cannot find the user, or if `pwdlib` says the submitted password does not match the stored password hash, it raises `401 Unauthorized`. On success, it calculates an expiration time from `EXP_TIME`, signs a JWT with the configured secret and algorithm, and returns:

```json
{
  "token": "<signed-jwt>"
}
```

The API expects the password value in the login request under the field name `hash_password`, but the client sends the plain password there. The server verifies it against the stored hash; it does not store or return the submitted password.

Use the returned token in the `Authorization` header for protected task endpoints.

## Check your understanding

Does the login request send the stored password hash, or the user's plain password?
