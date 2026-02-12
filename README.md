# tavcms

Bootstrap for the TavCMS Django monolith.

## Prerequisites
- Python 3.12.x

## Setup
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run database migrations
```bash
python manage.py migrate
```

## Create an admin user
```bash
python manage.py createsuperuser
```

## Run development server
```bash
python manage.py runserver
```

## Notes
- Settings module for local development defaults to `config.settings.dev`.
- Language-prefixed routes are enabled (for example `/fa/admin/` and `/en/admin/`).
