import re
from dataclasses import dataclass

from django.db import models
from django.utils.text import slugify

_PERSIAN_SLUG_RE = re.compile(r"[^\w\s\-\u0600-\u06FF]")
_MULTIPLE_DASH_RE = re.compile(r"-+")


@dataclass(frozen=True)
class SlugOptions:
    max_length: int = 70
    slug_field: str = "slug"
    title_field: str = "title"
    language_field: str = "language"


def get_configured_slug_max_length(default: int = 70) -> int:
    from apps.core.models import GlobalSettings

    try:
        settings_obj = GlobalSettings.objects.first()
    except Exception:
        return default

    if settings_obj and settings_obj.slug_max_length:
        return settings_obj.slug_max_length
    return default


def _normalize_persian(value: str) -> str:
    value = _PERSIAN_SLUG_RE.sub("", value)
    value = value.strip().replace("_", " ")
    value = re.sub(r"\s+", "-", value)
    value = _MULTIPLE_DASH_RE.sub("-", value)
    return value.strip("-")


def _normalize_english(value: str) -> str:
    return slugify(value, allow_unicode=False)


def normalize_slug(value: str, language: str | None = None) -> str:
    if language == "fa":
        return _normalize_persian(value)
    return _normalize_english(value).lower()


def _truncate_for_suffix(base_slug: str, max_length: int, suffix: str) -> str:
    if len(base_slug) + len(suffix) <= max_length:
        return base_slug
    truncated = base_slug[: max_length - len(suffix)].rstrip("-")
    return truncated or base_slug[: max_length - len(suffix)]


def generate_unique_slug(
    instance: models.Model,
    *,
    value: str,
    options: SlugOptions | None = None,
    language: str | None = None,
) -> str:
    options = options or SlugOptions()
    max_length = get_configured_slug_max_length(options.max_length)
    language = language or getattr(instance, options.language_field, None)
    base_slug = normalize_slug(value=value, language=language)
    if not base_slug:
        base_slug = "item"

    base_slug = base_slug[:max_length].rstrip("-")
    if not base_slug:
        base_slug = "item"

    model_class = instance.__class__
    queryset = model_class._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    lang_field = options.language_field
    has_lang_field = any(field.name == lang_field for field in model_class._meta.fields)
    if has_lang_field and language:
        queryset = queryset.filter(**{lang_field: language})

    slug_field = options.slug_field
    candidate = base_slug
    index = 1
    while queryset.filter(**{slug_field: candidate}).exists():
        index += 1
        suffix = f"-{index}"
        root = _truncate_for_suffix(base_slug, max_length, suffix)
        candidate = f"{root}{suffix}"

    return candidate
