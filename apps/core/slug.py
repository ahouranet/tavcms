import re
from typing import Any

from django.db.models import Model, QuerySet

DEFAULT_SLUG_MAX_LENGTH = 70

_FA_ALLOWED_CHARS = re.compile(r"[^0-9A-Za-z\u0600-\u06FF\s-]")
_EN_ALLOWED_CHARS = re.compile(r"[^0-9a-z\s-]")
_MULTI_SPACE = re.compile(r"\s+")
_MULTI_DASH = re.compile(r"-+")


def _sanitize_title(value: str, language: str) -> str:
    text = (value or "").strip()
    if language == "en":
        text = text.lower()
        text = _EN_ALLOWED_CHARS.sub("", text)
    else:
        text = _FA_ALLOWED_CHARS.sub("", text)

    text = _MULTI_SPACE.sub("-", text)
    text = _MULTI_DASH.sub("-", text).strip("-")
    return text


def _safe_truncate(base_slug: str, max_length: int) -> str:
    if len(base_slug) <= max_length:
        return base_slug
    return base_slug[:max_length].rstrip("-")


def build_unique_slug(
    *,
    title: str,
    language: str,
    model_class: type[Model],
    slug_field: str = "slug",
    language_field: str = "language",
    max_length: int = DEFAULT_SLUG_MAX_LENGTH,
    instance_pk: Any | None = None,
) -> str:
    base_slug = _sanitize_title(title, language) or "item"
    base_slug = _safe_truncate(base_slug, max_length)

    def exists(candidate: str) -> bool:
        filters = {slug_field: candidate}
        if language_field in {field.name for field in model_class._meta.get_fields()}:
            filters[language_field] = language

        queryset: QuerySet[Model] = model_class._default_manager.filter(**filters)
        if instance_pk is not None:
            queryset = queryset.exclude(pk=instance_pk)
        return queryset.exists()

    if not exists(base_slug):
        return base_slug

    counter = 2
    while True:
        suffix = f"-{counter}"
        allowed_len = max(max_length - len(suffix), 1)
        candidate_base = _safe_truncate(base_slug, allowed_len).rstrip("-") or "item"
        candidate = f"{candidate_base}{suffix}"
        if not exists(candidate):
            return candidate
        counter += 1
