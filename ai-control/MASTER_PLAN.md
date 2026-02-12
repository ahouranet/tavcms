# MASTER PLAN (Django CMS)

## Tech Versions
- **Python:** 3.12.x (پیشنهادی برای سازگاری اکوسیستم)
- **Django:** 5.2.x (LTS). در dependencies از `Django>=5.2,<5.3` استفاده شود.

> **Single Source of Truth برای مسیر اجرا**  
این سند مسیر کلی، قوانین ثابت (Invariants) و فازهای اجرای پروژه را مشخص می‌کند.  
پروژه یک **Django Monolith** است که اپ‌ها به صورت **app-by-app** و با **قراردادهای مشترک** (core contracts) توسعه داده می‌شوند.

## Goals (MVP)
- ساخت یک CMS چندزبانه با URL-prefix زبان (مثال: `/fa/...` و `/en/...`).
- تولید و مدیریت محتوا به صورت اپ‌به‌اپ (حداقل: Blog, Page, Product).
- ماژول‌های مشترک قابل استفاده در همه اپ‌های محتوا:
  - **core**: استاندارد چندزبانه (i18n URL)، استاندارد اسلاگ، ابزار تاریخ (شمسی/میلادی/قمری)، base models/mixins
  - **media_core**: مدیریت Asset و آپلود (MVP)
  - **seo_core**: متادیتا و sitemap پایه (MVP)
- پنل ادمین منظم، تست حداقلی برای قراردادهای مشترک و endpointهای اصلی.

## Non-goals (در MVP)
- Yoast-like analysis کامل در SEO (به فاز seo_plus منتقل می‌شود).
- Media processing پیشرفته (webp/compress/edit) در MVP (به media_plus منتقل می‌شود).
- Page Builder پیچیده (drag&drop کامل/نسخه‌بندی پیشرفته) در MVP (به builder_plus منتقل می‌شود).

## Invariants (قوانین غیرقابل شکستن)
### 1) زبان و مسیرها
- **تمام مسیرها باید زیر prefix زبان باشند، حتی زبان پیش‌فرض**: `/fa/...`, `/en/...` …
- افزودن زبان جدید باید فقط با:
  1) اضافه‌کردن به `LANGUAGES`
  2) تنظیم mapping «زبان → تقویم» از طریق ادمین
  انجام شود (بدون تغییر در اپ‌های محتوا).

### 2) اسلاگ (Slug) - استاندارد واحد
- هیچ اپ محتوایی حق ندارد سیستم اسلاگ جداگانه بسازد.  
  همه باید از **`core.slug`** استفاده کنند.
- هر مدل محتوایی که `title` دارد باید اسلاگ **اتوماتیک** داشته باشد (اگر کاربر دستی ننویسد).
- اسلاگ باید:
  - فاصله‌ها را به `-` تبدیل کند
  - کاراکترهای غیرمجاز را حذف کند
  - برای انگلیسی lowercase کند
  - برای فارسی حروف فارسی را حفظ کند (و فقط پاکسازی انجام دهد)
  - **یکتا باشد** و اگر تکراری شد `-2`, `-3` … اضافه کند
  - طول اسلاگ بر اساس سئو **قابل تنظیم** باشد و truncate امن انجام شود (قبل از suffix عددی)

### 3) تاریخ‌ها
- **ذخیره تاریخ در DB همیشه استاندارد (UTC/Gregorian)** است.
- نمایش تاریخ (Front و Admin display) بر اساس زبان (یا تنظیمات زبان) تغییر می‌کند:
  - مثال پیش‌فرض: `fa → jalali`، `en → gregorian`، `ar → hijri`
- هیچ اپی حق ندارد formatter تاریخ جداگانه بسازد؛ همه از **`core.dates`** استفاده می‌کنند.

### 4) قراردادهای مشترک (Shared Contracts)
- هر قابلیت مشترک باید ابتدا در core/contracts تعریف شود و سپس در اپ‌ها import شود.  
  مثال: SlugMixin, ContentBase, SEO mixin, Media Asset relation

### 5) Definition of Done (برای هر Task)
- تست‌های مرتبط پاس شود
- migrations درست
- lint/format رعایت شود
- `ai-control/state/context_pack.md` و `ai-control/state/next_steps.md` آپدیت شود
- یک بخش «How to verify» نوشته شود

## Milestones (فازها)
### Phase 0 — Bootstrap
- ساخت پروژه Django + ساختار settings + env/logging + DB
- ایجاد اپ `core` و قراردادهای i18n/slug/dates با تست

### Phase 1 — Shared Infrastructure (MVP)
- `media_core` (Asset, upload, validation)
- `seo_core` (meta fields + sitemap پایه + admin inline)

### Phase 2 — Content Apps (MVP)
- `blog` با استفاده از core+media+seo
- `page` با همان الگو
- `product` با همان الگو

### Phase 3 — Plus Features
- `media_plus` (webp/compress/edit pipeline)
- `seo_plus` (analysis مشابه Yoast، schema، checks)
- `builder_core/plus` (Page builder تکامل‌یافته)