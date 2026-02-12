# Context Pack (خلاصه وضعیت پروژه)
- Versions: Python 3.12.x, Django 5.2.x (dependencies: Django>=5.2,<5.3)

## North Star
Django 5.2 CMS چندزبانه با URL prefix زبان و قراردادهای مشترک برای slug/dates/media/seo.

## Invariants (خلاصه)
- تمام URLها prefix زبان دارند: /fa/... و /en/...
- slug فقط از core.slug
- تاریخ فقط از core.dates (DB همیشه UTC/Gregorian)
- اپ‌های محتوا فقط مصرف‌کننده قراردادها هستند، نه پیاده‌ساز.

## Planned Modules (MVP)
1) core (i18n/slug/dates + base mixins)
2) media_core (Asset/upload)
3) seo_core (meta fields + sitemap پایه)
4) blog, page, product (همه import کننده)

## Current Status
- Phase: 0 (Bootstrap)
- Next focus: ایجاد پروژه Django + ساختار settings و سپس core contracts (i18n/slug/dates)

## Open Questions / Assumptions
- پکیج ترجمه مدل‌ها: انتخاب در Phase0 (parler/modeltranslation/Custom).  
  MVP می‌تواند ابتدا URL-based language + ترجمه ساده template را پیاده کند و ترجمه مدل‌ها را در فاز بعدی تثبیت کند.
- تقویم‌ها: در MVP حداقل formatter در Front + نمایش در Admin list; ورودی Jalali/Hijri در admin می‌تواند فاز بعدی باشد.

## Immediate Next Steps
- Phase0-01 تا Phase0-04 (در next_steps.md)