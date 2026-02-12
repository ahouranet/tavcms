# Checkpoint: Phase0-03 — Core Shared Contracts

## خلاصه انجام‌شده
- سرویس استاندارد اسلاگ در `apps/core/slug.py` اضافه شد.
- میکسین مشترک `SlugMixin` در `apps/core/mixins.py` اضافه شد تا همه اپ‌های آینده از یک قرارداد واحد استفاده کنند.
- ابزارهای فرمت تاریخ در `apps/core/dates.py` اضافه شد (جلالی برای `fa`، میلادی برای `en`، پشتیبانی پایه برای `ar`).
- مدل Singleton تنظیمات سراسری با نام `GlobalSettings` در `apps/core/models.py` ساخته شد و در ادمین ثبت گردید.
- تست‌های حداقلی قراردادها در `apps/core/tests_slug.py` اضافه شد.

## فرضیات
- فاز «Phase0-03» طبق درخواست این تسک به معنی «Core Shared Contracts» در نظر گرفته شد.
- برای تقویم عربی (`ar`) پشتیبانی پایه (fallback) کافی است و فعلاً خروجی میلادی بازگردانده می‌شود.
- محدودیت طول اسلاگ از `GlobalSettings.slug_max_length` خوانده می‌شود و در صورت نبود تنظیمات، مقدار پیش‌فرض `70` استفاده می‌شود.

## فایل‌های تغییر یافته
- `apps/core/slug.py`
- `apps/core/mixins.py`
- `apps/core/dates.py`
- `apps/core/models.py`
- `apps/core/admin.py`
- `apps/core/tests_slug.py`
- `apps/core/migrations/0001_initial.py`
- `ai-control/checkpoints/Phase0-03.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/current_phase.json`
- `ai-control/state/next_steps.md`
- `ai-control/state/completed_modules.md`

## روش اعتبارسنجی (How to verify)
1. اجرای migration:
   - `python manage.py migrate`
2. اجرای تست‌های قرارداد:
   - `python manage.py test apps.core.tests apps.core.tests_slug`
3. اجرای سرور برای بررسی دستی:
   - `python manage.py runserver`
4. بررسی Singleton در ادمین:
   - ورود به `/admin/` و اطمینان از اینکه فقط یک رکورد `GlobalSettings` قابل ایجاد است.
