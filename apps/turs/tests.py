from django.test import TestCase
from .models import TravelSlider


class TravelSliderModelTest(TestCase):

    def setUp(self):
        self.slider = TravelSlider.objects.create(
            badge="Жаңы тур",
            title="Ысык-Көлгө саякат",
            description="Эң сонун эс алуу жайы",
            price=150,
            image_url="https://example.com/image.jpg",
            is_active=True
        )

    # __str__ методун текшерүү
    def test_slider_str(self):
        self.assertEqual(str(self.slider), "Ысык-Көлгө саякат")

    # title сакталдыбы текшерүү
    def test_slider_title(self):
        self.assertEqual(self.slider.title, "Ысык-Көлгө саякат")

    # price туура сакталдыбы
    def test_slider_price(self):
        self.assertEqual(self.slider.price, 150)

    # is_active default же мааниси
    def test_slider_is_active(self):
        self.assertTrue(self.slider.is_active)

    # image_url туурабы
    def test_slider_image_url(self):
        self.assertEqual(
            self.slider.image_url,
            "https://example.com/image.jpg"
        )