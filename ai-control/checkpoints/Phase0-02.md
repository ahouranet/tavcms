# Phase0-02 Checkpoint — زیرساخت مسیردهی و سوییچ زبان

## خلاصه
- مسیردهی عمومی پروژه با `i18n_patterns` تثبیت شد تا مسیرهای عمومی فقط با پیشوند زبان (`/fa/` و `/en/`) در دسترس باشند.
- مسیر ادمین طبق قرارداد فعلی به‌صورت بدون پیشوند زبان (`/admin/`) نگه داشته شد.
- endpoint استاندارد Django برای تغییر زبان (`/i18n/setlang/`) اضافه شد.
- قالب پایه و صفحه‌ی خانه‌ی حداقلی برای اعتبارسنجی سوییچ زبان و نمایش UI اولیه اضافه شد.
- تست‌های پایه برای بررسی مسیرهای `/fa/` و `/en/` و رفتار set_language اضافه شد.

## فرضیات
- در این فاز فقط زیرساخت مسیردهی و سوییچ زبان هدف است و وارد قراردادهای slug/dates نشده‌ایم.
- ذخیره زبان فعال در کوکی استاندارد `django_language` برای نیاز فعلی کافی است.

## فایل‌های تغییر یافته
- `config/urls.py`
- `apps/core/views.py`
- `apps/core/tests.py`
- `templates/base.html`
- `templates/home.html`
- `README.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/current_phase.json`
- `ai-control/state/next_steps.md`
- `ai-control/state/completed_modules.md`
- `ai-control/checkpoints/Phase0-02.md`

## روش بررسی
1. `python manage.py test apps.core`
2. `python manage.py runserver`
3. باز کردن `/fa/` و `/en/` و مشاهده صفحه‌ی خانه.
4. تغییر زبان از فرم هدر و بررسی ریدایرکت و کوکی `django_language`.
