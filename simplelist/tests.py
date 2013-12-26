import datetime

from django.utils import timezone
from django.test import TestCase

from simplelist.models import List

class ListMethodTests(TestCase):

    def test_was_created_recently_with_future_list(self):
        """
        was_created_recently() should return False for lists whose
        create_date is in the future
        """
        future_list = List(create_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_list.was_created_recently(), False)
