# چک‌پوینت Phase0-03 — راه‌اندازی PostgreSQL

## خلاصه
- تنظیمات پایگاه‌داده از SQLite به PostgreSQL در `config/settings/base.py` منتقل شد.
- پیکربندی اتصال DB با متغیرهای محیطی `POSTGRES_*` انجام شد تا محیط توسعه/استقرار قابل‌تنظیم باشد.
- وابستگی درایور PostgreSQL (`psycopg[binary]`) به `requirements.txt` اضافه شد.
- مستندات اجرای migration و ساخت superuser برای PostgreSQL در README به‌روز شد.
- فایل `.env.example` برای نمونه‌ی مقادیر اتصال DB اضافه شد.

## فرضیات
- PostgreSQL به‌عنوان DB استاندارد پروژه از همین فاز مبنا قرار می‌گیرد و SQLite دیگر مسیر اصلی نیست.
- مقدارهای پیش‌فرض `POSTGRES_*` صرفاً برای توسعه‌ی محلی هستند و در محیط واقعی باید override شوند.
- به دلیل محدودیت محیط اجرا، اجرای واقعی migration در این مرحله ممکن است نیازمند نصب وابستگی‌ها/دسترسی DB باشد.

## فایل‌های تغییر یافته
- `requirements.txt`
- `config/settings/base.py`
- `.env.example`
- `README.md`
- `ai-control/checkpoints/Phase0-03.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/current_phase.json`
- `ai-control/state/next_steps.md`
- `ai-control/state/completed_modules.md`

## نحوه‌ی بررسی
1. PostgreSQL را اجرا کنید و یک DB/USER مطابق متغیرهای محیطی بسازید.
2. وابستگی‌ها را نصب کنید: `pip install -r requirements.txt`
3. migration اولیه را اجرا کنید: `python manage.py migrate`
4. کاربر ادمین بسازید: `python manage.py createsuperuser`
5. سرور را اجرا کنید و ادمین را بررسی کنید: `python manage.py runserver` و مسیر `/admin/`
