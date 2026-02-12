from unittest.mock import patch

from django.contrib.admin.sites import AdminSite
from django.db import OperationalError
from django.test import RequestFactory, TestCase

from apps.core.admin import GlobalSettingsAdmin
from apps.core.models import GlobalSettings


class I18nRoutingTests(TestCase):
    def test_language_prefixed_routes_are_available(self):
        self.assertEqual(self.client.get("/fa/").status_code, 200)
        self.assertEqual(self.client.get("/en/").status_code, 200)

    def test_set_language_updates_language_cookie(self):
        response = self.client.post(
            "/i18n/setlang/",
            data={"language": "en", "next": "/en/"},
            follow=False,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/en/")
        self.assertEqual(response.cookies["django_language"].value, "en")


class GlobalSettingsAdminTests(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = GlobalSettingsAdmin(GlobalSettings, self.site)
        self.request = RequestFactory().get("/admin/")

    def test_has_add_permission_is_safe_without_table(self):
        with patch("apps.core.admin.GlobalSettings.objects.exists", side_effect=OperationalError):
            self.assertFalse(self.admin.has_add_permission(self.request))
