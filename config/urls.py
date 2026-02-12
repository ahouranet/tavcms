from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def healthcheck(_request):
    return HttpResponse("ok")


urlpatterns = [
    path("health/", healthcheck, name="healthcheck"),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", healthcheck, name="home"),
    prefix_default_language=True,
)
