from django.test import TestCase
from apps.coment.models import Review

class ReviewTest(TestCase):
    def test_review_create(self):
        review = Review.objects.create(
            name = "Колдонуучунун аты",
            stars = "5",
            text = "Бул абдан сонун саякат болду!",
        )

        self.assertEqual(
            review.name,
            "Колдонуучунун аты"
        )

        self.assertEqual(
           review.stars,"5",
        )

        self.assertEqual(
            review.text,
            "Бул абдан сонун саякат болду!",
        )


