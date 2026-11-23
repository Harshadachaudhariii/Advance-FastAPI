# 23 — Sending registration email

The app sends a registration confirmation email using FastAPI Mail. The mail configuration and `send_email()` function are in [mail.py](../../Task_Management_APP/src/utils/mail.py).

The helper loads `.env` values and configures Gmail SMTP on port `587`, with STARTTLS enabled. It reads `MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_FROM` from the environment. The message has the subject `Registration Confirmation`, uses an HTML body, and accepts a list of recipient addresses.

After saving a new user, the registration controller schedules the email helper with the new user's address. The mail helper is asynchronous, and its SMTP configuration is specific to Gmail in the current code.

Keep mail credentials in environment configuration, not in source files or committed notes. Email delivery depends on valid SMTP credentials and network access. The current helper does not add custom retry or failure-recovery logic.

## Check your understanding

Which three environment variables does the mail helper read for its SMTP account and sender?
