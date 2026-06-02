from django.test import TestCase 
from apps.tour_detail.models import TourDetail


class TourDetailTestCase(TestCase):
    def test_tourdetail_create(self):
        tourdetail = TourDetail.objects.create(
            full_description="text",
            location="Test Location",
            included="Test included",
            not_included="Test not included",
        )

        self.assertEqual(tourdetail.full_description, "text")