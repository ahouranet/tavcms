# Phase0-03 Checkpoint — قراردادهای مشترک Core

## خلاصه
- ماژول استاندارد اسلاگ در `apps/core/slug.py` اضافه شد تا تولید اسلاگ خودکار از عنوان، پاکسازی کاراکترها، و یکتاسازی زبان‌محور انجام شود.
- میکسین قابل‌استفاده‌ی `SlugMixin` در `apps/core/mixins.py` اضافه شد تا همه اپ‌های محتوا در فازهای بعدی از یک قرارداد واحد استفاده کنند.
- ابزار تاریخ در `apps/core/dates.py` اضافه شد و دو API اصلی `format_date` و `format_datetime` برای زبان‌های `fa`, `en`, `ar` آماده شد.
- مدل singleton تنظیمات سراسری با نام `GlobalSettings` در `apps/core/models.py` اضافه شد و در ادمین ثبت شد.
- تست‌های حداقلی قراردادهای اسلاگ و تاریخ در `apps/core/tests_slug.py` اضافه شد.

## فرضیات
- برای `ar` تبدیل تاریخ هجری به‌صورت تقریبی پیاده‌سازی شد و در صورت نیاز به دقت تقویمی بالا، در فازهای بعدی بهبود داده می‌شود.
- مقدار پیش‌فرض `slug_max_length=70` به‌عنوان قرارداد اولیه نگه داشته شد و از طریق `GlobalSettings` قابل مدیریت است.
- در این فاز فقط قراردادهای مشترک Core پیاده‌سازی شد و هیچ اپ محتوایی جدید ساخته نشد.

## فایل‌های تغییر یافته
- `apps/core/slug.py`
- `apps/core/mixins.py`
- `apps/core/dates.py`
- `apps/core/models.py`
- `apps/core/admin.py`
- `apps/core/tests_slug.py`
- `apps/core/migrations/0001_initial.py`
- `apps/core/migrations/0002_slugcontractsample.py`
- `apps/core/migrations/__init__.py`
- `ai-control/checkpoints/Phase0-03.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/current_phase.json`
- `ai-control/state/next_steps.md`
- `ai-control/state/completed_modules.md`

## روش بررسی
1. `python manage.py migrate`
2. `python manage.py test apps.core`
3. `python manage.py runserver`
4. ورود به `/admin/` و بررسی امکان ساخت فقط یک رکورد برای تنظیمات سراسری.
