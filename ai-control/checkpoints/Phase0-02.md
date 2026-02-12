# چک‌پوینت Phase0-02 — پایه‌ی i18n و تعویض زبان

## خلاصه
- مسیرهای عمومی پروژه زیر `i18n_patterns` قرار گرفتند تا فقط با پیشوند زبان (`/fa/` و `/en/`) در دسترس باشند.
- مسیر ادمین طبق نیاز این فاز به‌صورت بدون پیشوند زبان روی `/admin/` نگه داشته شد.
- endpoint استاندارد Django برای `set_language` فعال شد.
- یک UI مینیمال برای تعویض زبان در قالب پایه اضافه شد.
- صفحه‌ی اصلی مینیمال برای تست دستی تعویض زبان ساخته شد.
- تست‌های حداقلی برای مسیرهای زبان‌دار و تغییر زبان از طریق session اضافه شد.

## فرضیات
- در این فاز فقط پایه‌ی URL-based i18n لازم است و ترجمه‌ی کامل رشته‌ها/فایل‌های po در فازهای بعدی تکمیل می‌شود.
- نگه‌داشتن ادمین روی `/admin/` بدون پیشوند زبان، تصمیم فعلی بر اساس دستور این تسک است.
- ترتیب Phase0-02 صرفاً شامل i18n foundation است و وارد تنظیمات PostgreSQL (Phase0-03) نمی‌شویم.

## فایل‌های تغییر یافته
- `config/urls.py`
- `apps/core/views.py`
- `apps/core/tests.py`
- `templates/base.html`
- `templates/home.html`
- `templates/includes/language_switcher.html`
- `README.md`
- `ai-control/checkpoints/Phase0-02.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/current_phase.json`
- `ai-control/state/next_steps.md`
- `ai-control/state/completed_modules.md`

## نحوه‌ی بررسی
1. وابستگی‌ها را نصب کنید.
2. دستور `python manage.py migrate` را اجرا کنید.
3. دستور `python manage.py runserver` را اجرا کنید.
4. آدرس‌های زیر باید پاسخ 200 بدهند:
   - `/fa/`
   - `/en/`
5. فرم تعویض زبان را روی صفحه‌ی اصلی استفاده کنید و تغییر مسیر/زبان فعال را بررسی کنید.
6. تست‌ها را اجرا کنید:
   - `python manage.py test apps.core`
