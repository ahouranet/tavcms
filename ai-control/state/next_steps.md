> Note: هنگام ساخت requirements، حتماً Django را روی **5.2.x** پین کن: `Django>=5.2,<5.3`.

# Next Steps (Backlog خرد شده)

## Phase 0 — Bootstrap
- [ ] Phase0-01: ایجاد پروژه Django + ساختار پوشه‌ها (config/apps) + gitignore
- [ ] Phase0-02: settings split (base/dev/prod) + env loader + logging پایه
- [ ] Phase0-03: راه‌اندازی DB (PostgreSQL) + migrate اولیه + superuser دستورالعمل
- [ ] Phase0-04: فعال‌سازی i18n URL prefix برای همه routeها (/fa/, /en/...) + تست routing
- [ ] Phase0-05: ساخت اپ `core` با قراردادها:
  - [ ] core.slug: service + SlugMixin (fa/en rules, uniqueness per language, max length)
  - [ ] core.dates: format_date/format_datetime با mapping زبان→تقویم (fa jalali, en gregorian, ar hijri)
  - [ ] core.i18n: helper برای language current + template selection helper (اختیاری)
- [ ] Phase0-06: ساخت مدل تنظیمات singleton در core (default language, lang→calendar, slug_max_len, prefix_default_lang)
- [ ] Phase0-07: تست‌های حداقلی برای slug و dates و i18n prefix
- [ ] Phase0-08: ADR جدید: «Shared contracts & no re-implementation»

## Phase 1 — Shared Infrastructure (MVP)
- [ ] Phase1-01: media_core (Asset model + upload/validation + admin)
- [ ] Phase1-02: seo_core (SEOData model + admin inline + sitemap پایه)