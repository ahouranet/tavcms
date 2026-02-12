# Next Steps (Backlog خرد شده)

## Phase 0 — Bootstrap
- [x] Phase0-01: ایجاد پروژه Django + ساختار پوشه‌ها (config/apps) + gitignore
- [x] Phase0-02: زیرساخت حداقلی i18n routing + language switch + قالب پایه + تست
- [x] Phase0-03: قراردادهای مشترک core
  - [x] core.slug: service + SlugMixin (fa/en rules, uniqueness per language, max length)
  - [x] core.dates: format_date/format_datetime با mapping زبان→تقویم (fa jalali, en gregorian, ar basic)
  - [x] مدل تنظیمات singleton در core (default language, lang→calendar, slug_max_length)
  - [x] تست‌های حداقلی slug و dates
- [ ] Phase0-04: تکمیل helperهای i18n در core (خواندن زبان جاری + helper انتخاب قالب)
- [ ] Phase0-05: یکپارچه‌سازی مصرف `GlobalSettings` در لایه‌های نمایشی/ادمین (calendar mapping در UI)
- [ ] Phase0-06: ADR جدید: «Shared contracts & no re-implementation»

## Phase 1 — Shared Infrastructure (MVP)
- [ ] Phase1-01: media_core (Asset model + upload/validation + admin)
- [ ] Phase1-02: seo_core (SEOData model + admin inline + sitemap پایه)
