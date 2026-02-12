# AI INSTRUCTIONS (برای Codex)


## Version Pinning
- پروژه باید با **Python 3.12.x** و **Django 5.2.x (LTS)** ساخته شود.
- در dependency file حتماً از **`Django>=5.2,<5.3`** استفاده کن (نه بازه‌های قدیمی مثل `<5.1`).

> هدف: Codex باید پروژه را مرحله‌به‌مرحله، بدون اختراع ساختارهای جداگانه، و مطابق قراردادهای مشترک بسازد.

## Always Read First
قبل از شروع هر Task این فایل‌ها را بخوان و بر اساس آنها تصمیم بگیر:
- `ai-control/MASTER_PLAN.md`
- `ai-control/ARCHITECTURE.md`
- `ai-control/state/context_pack.md`
- `ai-control/state/next_steps.md`
- `ai-control/CODING_STANDARDS.md`
- `ai-control/SECURITY_CHECKLIST.md`

## Rules (Non-negotiable)
1) **One task at a time**  
   هر بار فقط یک Task مشخص را انجام بده. کار بزرگ را به چند Task خرد کن.
2) **No re-implementation**  
   هیچ اپ محتوایی حق ندارد i18n/slug/dates/media/seo را دوباره پیاده‌سازی کند. فقط import از اپ‌های مشترک.
3) **Assumptions policy**  
   اگر ابهام وجود داشت، توقف نکن. فرضیات را شفاف در checkpoint بنویس و ادامه بده.
4) **After each task**  
   - تست‌های مرتبط را اجرا/آپدیت کن
   - `ai-control/state/context_pack.md` را به‌روز کن (10–15 خط)
   - `ai-control/state/next_steps.md` را به‌روز کن
   - `ai-control/state/completed_modules.md` را به‌روز کن
   - یک `ai-control/checkpoints/<task-id>.md` بساز

## Shared Contracts you MUST create first
### Phase0 Contracts (core)
- i18n URL prefix: همه مسیرها زیر `/fa/`, `/en/`…
- slug: Slug service + SlugMixin با قوانین فارسی/انگلیسی و یکتایی در زبان
- dates: formatter واحد با mapping زبان→تقویم و نمایش مناسب

## Deliverable format
برای هر Task خروجی بده:
- فایل‌های تغییر یافته
- خلاصه تغییرات
- How to verify (چک‌لیست کوتاه)
- تغییرات state/checkpoint