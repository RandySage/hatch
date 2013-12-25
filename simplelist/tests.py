import datetime

from django.utils import timezone
from django.test import TestCase

from simplelist.models import Specification

class SpecificationMethodTests(TestCase):

    def test_was_created_recently_with_future_specification(self):
        """
        was_created_recently() should return False for specifications whose
        create_date is in the future
        """
        future_specification = Specification(create_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_specification.was_created_recently(), False)
