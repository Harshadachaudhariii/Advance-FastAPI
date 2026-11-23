# 19 — Validating a token

Task routes use `is_authenticate()` from [helpers.py](../../Task_Management_APP/src/utils/helpers.py) as a FastAPI dependency. The helper reads the request's `Authorization` header, extracts the last space-separated part, and decodes it with the configured JWT secret and algorithm.

The decoded payload's `_id` is used to look up a `UserModel`. If the header is missing, the token cannot be decoded, or the user no longer exists, the helper raises `401 Unauthorized`. A valid token returns the user model for use by the route and controller.

The client-facing convention is:

```http
Authorization: Bearer <token>
```

The helper does not use FastAPI's OAuth2 bearer-token dependency; it manually parses the header. There is also a similar token-validation function in [user/controller.py](../../Task_Management_APP/src/user/controller.py), used by `/user/is_auth`. These two implementations currently duplicate logic.

## Check your understanding

After decoding a token, which payload field does the helper use to find the user?
