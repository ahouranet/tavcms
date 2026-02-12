# tavcms

بوت‌استرپ اولیه‌ی پروژه‌ی Django برای TavCMS.

## پیش‌نیازها
- Python 3.12.x

## راه‌اندازی محیط
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

## الگوی مسیرهای چندزبانه
- مسیرهای عمومی فقط با پیشوند زبان در دسترس هستند.
- نمونه‌ها:
  - `http://127.0.0.1:8000/fa/`
  - `http://127.0.0.1:8000/en/`
- پنل ادمین فعلاً بدون پیشوند زبان روی مسیر زیر است:
  - `http://127.0.0.1:8000/admin/`

## تعویض زبان
- در قالب پایه یک فرم ساده‌ی تعویض زبان قرار داده شده است.
- فرم به endpoint استاندارد Django (`set_language`) ارسال می‌شود.
- زبان انتخاب‌شده در session/cookie ذخیره می‌شود و کاربر به مسیر `next` برمی‌گردد.

## افزودن زبان جدید
1. در `config/settings/base.py` زبان جدید را به `LANGUAGES` اضافه کنید.
2. فایل‌های ترجمه‌ی مربوط را در مسیر `locale/` ایجاد/به‌روزرسانی کنید.
3. از طریق UI تعویض زبان، زبان جدید به‌صورت خودکار نمایش داده می‌شود.
