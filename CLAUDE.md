# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Course project following the [Python Django - The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide) Udemy course by Max. Currently implements a **Monthly Challenges** app.

## Commands

Dependencies are managed with `uv`. The Django project lives in `monthly_challenges/` — all `manage.py` commands run from there.

```bash
# Install dependencies
uv sync

# Run dev server
cd monthly_challenges && uv run python manage.py runserver

# Run migrations
cd monthly_challenges && uv run python manage.py migrate

# Run tests
cd monthly_challenges && uv run python manage.py test

# Run a single test
cd monthly_challenges && uv run python manage.py test challenges.tests.TestClassName.test_method_name
```

## Architecture

```
monthly_challenges/          # Django project root
  monthly_challenges/        # Project package (settings, root URLs, wsgi/asgi)
  challenges/                # Django app — the only app so far
    views.py                 # All view logic; challenge data is a plain dict (no DB models yet)
    urls.py                  # App-level URL patterns
    models.py                # Empty — no models yet
    tests.py                 # Empty — tests not yet written
```

**URL routing**: The root URLconf (`monthly_challenges/urls.py`) delegates `/challenges/` to the app's URLconf, which handles two patterns:
- `<str:month>` — returns the challenge text for a named month
- `<int:month>` — redirects to the named-month URL by converting the number to a month name

**Data layer**: Challenge data is currently a hardcoded dict in `views.py`. No database models are in use yet.

**Database**: SQLite (`db.sqlite3`) in the `monthly_challenges/` directory. Django's built-in apps (auth, sessions, etc.) are installed but the `challenges` app itself has no migrations.
