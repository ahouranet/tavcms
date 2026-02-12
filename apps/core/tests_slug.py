from datetime import datetime

from django.db import connection, models
from django.test import TestCase, TransactionTestCase
from django.test.utils import isolate_apps

from apps.core.dates import format_date, format_datetime
from apps.core.mixins import SlugMixin
from apps.core.models import GlobalSettings


@isolate_apps("apps.core")
class SlugContractTests(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        class Content(SlugMixin):
            title = models.CharField(max_length=200)
            language = models.CharField(max_length=5, default="fa")

            class Meta:
                app_label = "core"
                managed = True

        cls.Content = Content
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Content)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(cls.Content)
        super().tearDownClass()

    def test_slug_auto_generated_from_title(self):
        item = self.Content.objects.create(title="سلام دنیا", language="fa")
        self.assertEqual(item.slug, "سلام-دنیا")

    def test_slug_uniqueness_with_language_scope(self):
        self.Content.objects.create(title="سلام دنیا", language="fa")
        duplicate_fa = self.Content.objects.create(title="سلام دنیا", language="fa")
        en_item = self.Content.objects.create(title="Hello World", language="en")
        en_duplicate = self.Content.objects.create(title="Hello World", language="en")

        self.assertEqual(duplicate_fa.slug, "سلام-دنیا-2")
        self.assertEqual(en_item.slug, "hello-world")
        self.assertEqual(en_duplicate.slug, "hello-world-2")

    def test_slug_max_length_truncation_keeps_suffix_safe(self):
        GlobalSettings.objects.create(
            default_language="fa",
            slug_max_length=10,
            language_calendar_mapping={"fa": "jalali", "en": "gregorian"},
        )
        self.Content.objects.create(title="hello world extra", language="en")
        second = self.Content.objects.create(title="hello world extra", language="en")

        self.assertEqual(len(second.slug), 10)
        self.assertTrue(second.slug.endswith("-2"))


class DateFormattingTests(TestCase):
    def test_formatters_respect_language(self):
        dt = datetime(2024, 3, 20, 14, 30)

        self.assertEqual(format_date(dt, "fa"), "1403-01-01")
        self.assertEqual(format_datetime(dt, "fa"), "1403-01-01 14:30")
        self.assertEqual(format_date(dt, "en"), "2024-03-20")
        self.assertEqual(format_datetime(dt, "en"), "2024-03-20 14:30")
