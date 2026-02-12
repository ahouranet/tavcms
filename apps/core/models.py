from django.core.exceptions import ValidationError
from django.db import models


class CoreScaffold(models.Model):
    """Placeholder model for initial app scaffold."""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class GlobalSettings(models.Model):
    default_language = models.CharField(max_length=10, default="fa")
    slug_max_length = models.PositiveIntegerField(default=70)
    language_calendar_mapping = models.JSONField(
        default=dict,
        help_text="Mapping زبان به تقویم. مثال: {'fa': 'jalali', 'en': 'gregorian'}",
    )

    class Meta:
        verbose_name = "Global Settings"
        verbose_name_plural = "Global Settings"

    def clean(self):
        if self.__class__.objects.exclude(pk=self.pk).exists():
            raise ValidationError("Only one GlobalSettings instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return "تنظیمات سراسری"
