# FastAPI learning-notes workflow

When the user says **"u start"**, begin the learning-notes workflow:

1. Scan the current project source, dependency/configuration files, and existing files in `notes/`. Treat the code that exists now as the source of truth; do not assume a topic has been implemented just because it appears in the lesson outline.
2. Keep `notes/03_first_api.md` as a live, code-grounded note while the user is working on the first API in `main.py`. On each "u start" request during this stage, refresh note 03 to match the current `main.py`, including when the user has cleared or rewritten it. Do not advance to note 04 unless the user asks to move on or the current request clearly starts a new lesson.
3. Explain concepts using the actual project code and its current state. If the code does not support a lesson yet, say so rather than inventing implementation details. Write or update only the matching `notes/NN_*.md` file and any earlier note made factually stale by the code change. Preserve numbering and filenames, and avoid replacing unrelated notes.
4. Work interactively: give a brief explanation of what you found, write the note, then ask one short comprehension or hands-on question and wait for the user's response before continuing to another lesson. Do not ask for approval to write a note that is clearly supported by the code.
5. If the next lesson is ambiguous or the project has changed in a way that makes the right note unclear, ask one focused question before writing.

The user asked for notes 01 and 02 to be authored initially. They are in `notes/01_introduction.md` and `notes/02_setup.md`. The user is currently iterating on the first API in `main.py` and wants note 03 refreshed from that file whenever they say "u start".

## Lesson outline

1. `notes/01_introduction.md` — Introduction
2. `notes/02_setup.md` — Setup
3. `notes/03_first_api.md` — First API
4. `notes/04_path_query_params.md` — Path and query parameters
5. `notes/05_http_methods.md` — HTTP methods
6. `notes/06_pydantic.md` — Pydantic
7. `notes/07_project_structure.md` — Project structure
8. `notes/08_postgresql.md` — PostgreSQL
9. `notes/09_sqlalchemy_models.md` — SQLAlchemy models
10. `notes/10_create_data.md` — Creating data
11. `notes/11_read_data.md` — Reading data
12. `notes/12_fetch_by_id.md` — Fetching by ID
13. `notes/13_update_delete.md` — Updating and deleting
14. `notes/14_best_practices.md` — Best practices
15. `notes/15_jwt_auth.md` — JWT authentication
16. `notes/16_registration.md` — Registration
17. `notes/17_validation.md` — Validation
18. `notes/18_login.md` — Login
19. `notes/19_token_auth.md` — Token authentication
20. `notes/20_protected_routes.md` — Protected routes
21. `notes/21_relationships.md` — Relationships
22. `notes/22_user_tasks.md` — User tasks
23. `notes/23_email.md` — Email
24. `notes/24_background_tasks.md` — Background tasks
25. `notes/25_revision.md` — Revision
26. `notes/26_ai_agent_langchain.md` — AI agent with LangChain
