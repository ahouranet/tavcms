from django.db import models

from apps.core.slug import SlugOptions, generate_unique_slug


class SlugMixin(models.Model):
    slug = models.SlugField(max_length=70, blank=True)

    slug_options = SlugOptions()

    class Meta:
        abstract = True

    def get_slug_source_value(self) -> str:
        return getattr(self, self.slug_options.title_field, "")

    def build_slug(self) -> str:
        source_value = self.slug or self.get_slug_source_value()
        return generate_unique_slug(
            self,
            value=source_value,
            options=self.slug_options,
            language=getattr(self, self.slug_options.language_field, None),
        )

    def save(self, *args, **kwargs):
        if not getattr(self, self.slug_options.slug_field):
            self.slug = self.build_slug()
        super().save(*args, **kwargs)
