from django.test import TestCase


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
