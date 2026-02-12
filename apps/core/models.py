from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.core.mixins import SlugMixin


class CoreScaffold(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class GlobalSettings(models.Model):
    default_language = models.CharField(max_length=8, choices=settings.LANGUAGES, default="fa")
    slug_max_length = models.PositiveSmallIntegerField(
        default=70,
        validators=[MinValueValidator(10), MaxValueValidator(200)],
    )
    language_calendar_mapping = models.JSONField(
        default=dict,
        help_text="نگاشت زبان به تقویم. مثال: {'fa': 'jalali', 'en': 'gregorian', 'ar': 'hijri'}",
    )

    class Meta:
        verbose_name = "تنظیمات سراسری"
        verbose_name_plural = "تنظیمات سراسری"

    def clean(self):
        if self.pk is None and GlobalSettings.objects.exists():
            raise ValidationError("فقط یک رکورد تنظیمات سراسری مجاز است.")

    def save(self, *args, **kwargs):
        if not self.language_calendar_mapping:
            self.language_calendar_mapping = {
                "fa": "jalali",
                "en": "gregorian",
                "ar": "hijri",
            }
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Global Settings"


class SlugContractSample(SlugMixin):
    """مدل نمونه برای اعتبارسنجی قرارداد اسلاگ در تست‌ها."""

    class Meta:
        verbose_name = "نمونه قرارداد اسلاگ"
        verbose_name_plural = "نمونه‌های قرارداد اسلاگ"

