# 15 — JWT authentication

The app issues a JSON Web Token after a successful username/password login. The login route in [router.py](../../Task_Management_APP/src/user/router.py) sends the request to `user_login()` in [controller.py](../../Task_Management_APP/src/user/controller.py).

After verifying the user and password, the controller creates an expiration time using `EXP_TIME` minutes and encodes a JWT payload:

```python
token = jwt.encode(
    {"_id": user.id, "exp": exp_time.timestamp()},
    settings.SECRETE_KEY,
    settings.ALGORITHM,
)
return {"token": token}
```

The payload contains the user's database ID in `_id` and the token expiration in `exp`. The signing key and algorithm come from application settings. The current setting name is spelled `SECRETE_KEY` in the code.

The API returns the token as JSON. Clients should keep it private and send it in an `Authorization: Bearer <token>` header when calling protected task routes. Anyone who obtains a valid token can act as its associated user until the token expires.

## Check your understanding

Which user information is stored in this app's JWT payload?
