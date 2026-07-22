from django.test import TestCase

from .models import UncertainDate


class UncertainDateDisplayTests(TestCase):
    def test_display_uses_full_date_when_available(self):
        uncertain_date = UncertainDate(year=1200, month=6, day=15)

        self.assertEqual(uncertain_date.display(), "1200-06-15")

    def test_display_falls_back_to_year_when_only_year_is_known(self):
        uncertain_date = UncertainDate(year=1200)

        self.assertEqual(uncertain_date.display(), "1200")
