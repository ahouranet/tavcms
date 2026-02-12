# tavcms

پروژه‌ی TavCMS یک Django Monolith چندزبانه است.

## پیش‌نیازها
- Python 3.12.x

## راه‌اندازی
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## اجرای مایگریشن‌ها
```bash
python manage.py migrate
```

## ساخت کاربر ادمین
```bash
python manage.py createsuperuser
```

## اجرای سرور توسعه
```bash
python manage.py runserver
```

## رفتار مسیرهای چندزبانه
- تمام مسیرهای عمومی زیر پیشوند زبان قرار دارند.
- نمونه‌ها:
  - `http://127.0.0.1:8000/fa/`
  - `http://127.0.0.1:8000/en/`
- مسیر ادمین طبق قرارداد فعلی بدون پیشوند زبان است:
  - `http://127.0.0.1:8000/admin/`

## تغییر زبان
- در هدر صفحه‌ی اصلی یک فرم ساده‌ی تغییر زبان وجود دارد.
- فرم به endpoint استاندارد Django یعنی `/i18n/setlang/` ارسال می‌شود.
- زبان انتخاب‌شده در کوکی استاندارد `django_language` ذخیره می‌شود.

## افزودن زبان جدید
1. در `config/settings/base.py` زبان جدید را به `LANGUAGES` اضافه کنید.
2. در صورت نیاز، ترجمه‌ها را در مسیر `locale/` ایجاد کنید.
3. پس از افزودن زبان، مسیرهای پیشونددار همان زبان به‌صورت خودکار با `i18n_patterns` فعال می‌شوند.
