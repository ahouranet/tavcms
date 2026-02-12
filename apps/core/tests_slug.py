from datetime import datetime

from django.test import TestCase

from apps.core.dates import format_date, format_datetime
from apps.core.models import SlugContractSample


class SlugAndDatesTests(TestCase):
    def test_slug_auto_generation(self):
        item = SlugContractSample.objects.create(title="سلام دنیا", language="fa")
        self.assertEqual(item.slug, "سلام-دنیا")

    def test_slug_uniqueness_suffix_is_language_aware(self):
        first = SlugContractSample.objects.create(title="سلام دنیا", language="fa")
        second = SlugContractSample.objects.create(title="سلام دنیا", language="fa")
        english = SlugContractSample.objects.create(title="Hello World", language="en")
        english_second = SlugContractSample.objects.create(title="Hello World", language="en")

        self.assertEqual(first.slug, "سلام-دنیا")
        self.assertEqual(second.slug, "سلام-دنیا-2")
        self.assertEqual(english.slug, "hello-world")
        self.assertEqual(english_second.slug, "hello-world-2")

    def test_slug_max_length_truncation(self):
        long_title = "very long english title " * 10
        item = SlugContractSample.objects.create(title=long_title, language="en")
        duplicate = SlugContractSample.objects.create(title=long_title, language="en")

        self.assertLessEqual(len(item.slug), 70)
        self.assertLessEqual(len(duplicate.slug), 70)
        self.assertTrue(duplicate.slug.endswith("-2"))

    def test_date_formatting_by_language(self):
        dt = datetime(2026, 2, 12, 14, 30)

        self.assertEqual(format_date(dt, "en"), "2026-02-12")
        self.assertRegex(format_date(dt, "fa"), r"^\d{4}/\d{2}/\d{2}$")
        self.assertRegex(format_date(dt, "ar"), r"^\d{4}/\d{2}/\d{2}$")
        self.assertRegex(format_datetime(dt, "fa"), r"^\d{4}/\d{2}/\d{2} 14:30$")
