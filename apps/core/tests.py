from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse


class I18nRoutingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_language_prefixed_routes_are_accessible(self):
        response_fa = self.client.get("/fa/")
        response_en = self.client.get("/en/")

        self.assertEqual(response_fa.status_code, 200)
        self.assertEqual(response_en.status_code, 200)

    def test_set_language_updates_session(self):
        response = self.client.post(
            reverse("set_language"),
            data={"language": "en", "next": "/en/"},
            follow=False,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/en/")
        self.assertEqual(self.client.session.get(settings.LANGUAGE_COOKIE_NAME), "en")
