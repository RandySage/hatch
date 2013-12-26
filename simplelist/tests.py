import datetime

from django.utils import timezone
from django.test import TestCase

from simplelist.models import Collection

class CollectionMethodTests(TestCase):

    def test_was_created_recently_with_future_collection(self):
        """
        was_created_recently() should return False for collections whose
        create_date is in the future
        """
        future_collection = Collection(create_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_collection.was_created_recently(), False)
