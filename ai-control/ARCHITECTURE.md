# ARCHITECTURE (Django Monolith)

- Python 3.12.x
## Tech Stack
- Django (monolith) — **Django 5.2.x (LTS)**
- DB: PostgreSQL
- Cache/Queue (اختیاری در MVP): Redis
- Storage: Local (dev) / قابل تغییر به S3 (بعداً)

## Project Layout (پیشنهادی)
- `config/`
  - `settings/`
    - `base.py`
    - `dev.py`
    - `prod.py`
  - `urls.py`
  - `wsgi.py` / `asgi.py`
- `apps/`
  - `core/`  ← قراردادهای مشترک (i18n/slug/dates/base models)
  - `media_core/`
  - `seo_core/`
  - `blog/`
  - `page/`
  - `product/`
- `templates/`
  - `fa/` و `en/` (قابل override؛ اگر تم‌های متفاوت نیاز شد)
- `static/`, `media/`

## i18n & URL prefix
- استفاده از `LocaleMiddleware`
- استفاده از `i18n_patterns` یا رویکرد معادل برای اینکه **همه URLها زیر prefix زبان باشند**
- زبان پیش‌فرض: `fa` (قابل تغییر از طریق تنظیمات ادمین)

## Shared Contracts (core)
### core.slug
- یک service + mixin برای تولید slug
- یکتایی slug **در محدوده زبان** (و در صورت نیاز scope قابل توسعه)

### core.dates
- API واحد: `format_date(dt, lang)` و `format_datetime(dt, lang)`
- ذخیره در DB: UTC/Gregorian
- نمایش: بر اساس mapping زبان → تقویم از تنظیمات ادمین

### core.i18n
- helper برای خواندن زبان فعلی از request
- ابزارهای کمکی برای template selection per language (در صورت نیاز)

## Settings & Admin Settings
- یک مدل تنظیمات (singleton) در ادمین برای:
  - default language
  - language → calendar mapping
  - slug max length
  - prefix default language (پیش‌فرض ON)

## Templates per language
- الگوی مسیر قالب‌ها: `templates/<lang>/...`
- fallback: اگر قالب `<lang>` نبود، از `templates/default/...` یا `templates/base/...` استفاده شود (قابل پیاده‌سازی در فاز اولیه)