from django.db import models


class CoreScaffold(models.Model):
    """Placeholder model for initial app scaffold."""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
