from django.db import models

from apps.core.slug import DEFAULT_SLUG_MAX_LENGTH, build_unique_slug


class SlugMixin(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=70, blank=True)
    language = models.CharField(max_length=8, default="fa")

    class Meta:
        abstract = True

    def get_slug_max_length(self) -> int:
        field = self._meta.get_field("slug")
        return field.max_length or DEFAULT_SLUG_MAX_LENGTH

    def generate_slug(self) -> str:
        return build_unique_slug(
            title=self.title,
            language=self.language,
            model_class=self.__class__,
            max_length=self.get_slug_max_length(),
            instance_pk=self.pk,
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)
