from django.contrib import admin
from django.db import OperationalError, ProgrammingError

from apps.core.models import GlobalSettings


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ("default_language", "slug_max_length")

    def has_add_permission(self, request):
        try:
            if GlobalSettings.objects.exists():
                return False
        except (OperationalError, ProgrammingError):
            return False
        return super().has_add_permission(request)
