# Phase0-01 Checkpoint — Django Bootstrap

## Summary
- Bootstrapped Django project structure using `config/` and split settings modules (`base`, `dev`, `prod`).
- Added initial `apps/core` scaffold as the shared contracts host (no feature implementation yet).
- Added dependency pin in `requirements.txt` with `Django>=5.2,<5.3`.
- Enabled i18n groundwork with `LocaleMiddleware`, `LANGUAGES`, and language-prefixed URLs via `i18n_patterns`.
- Added a minimal `README.md` with setup, migrate, createsuperuser, and run instructions.

## Assumptions
- For Phase0-01, SQLite is acceptable as a temporary local bootstrap DB; PostgreSQL wiring is deferred to Phase0-03 per backlog order.
- A placeholder root/health route is acceptable to validate language-prefixed URL wiring before content apps are added.
- Production host and secret values are placeholders in this phase and will be environment-driven in Phase0-02.

## Files Changed
- `.gitignore`
- `requirements.txt`
- `README.md`
- `manage.py`
- `config/__init__.py`
- `config/asgi.py`
- `config/wsgi.py`
- `config/urls.py`
- `config/settings/__init__.py`
- `config/settings/base.py`
- `config/settings/dev.py`
- `config/settings/prod.py`
- `apps/__init__.py`
- `apps/core/__init__.py`
- `apps/core/apps.py`
- `apps/core/models.py`
- `apps/core/admin.py`
- `apps/core/tests.py`
- `apps/core/views.py`
- `ai-control/checkpoints/Phase0-01.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/current_phase.json`
- `ai-control/state/next_steps.md`
- `ai-control/state/completed_modules.md`

## How to Verify
1. Create and activate Python 3.12 virtualenv.
2. Install dependencies from `requirements.txt`.
3. Run `python manage.py check`.
4. Run `python manage.py migrate`.
5. Run `python manage.py runserver` and verify:
   - `/fa/admin/` loads
   - `/en/admin/` loads
   - `/health/` returns `ok`
