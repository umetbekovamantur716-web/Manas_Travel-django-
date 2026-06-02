from django.test import TestCase
from apps.about.models import AboutUs

class AboutUsTest(TestCase):
    def test_aboutus_create(self):
        aboutus = AboutUs.objects.create(
            title ="Биз жөнүндө",
            description ="Компания жөнүндө толук маалымат",
            stat_clients = "Кардарлардын саны",
            stat_tours  = "Жылдык тажрыйба",
            fact_1_icon ="Факт 1 иконка",
            fact_1_number = "Факт 1 сан",
            fact_1_text = "Раз мы поднимались на вершины Тянь-Шаня с нашими туристами."

        )

        self.assertEqual(
            aboutus.title, 
            "Биз жөнүндө" 
        )

        self.assertEqual(
            aboutus.description,
            "Компания жөнүндө толук маалымат" 
        )
        self.assertEqual(
            aboutus.stat_clients, 
            "Кардарлардын саны"
        )

        self.assertEqual(
            aboutus.stat_tours,
            "Жылдык тажрыйба",
        )

        self.assertEqual(
            aboutus.fact_1_icon,
            "Факт 1 иконка",
        )

        self.assertEqual(
            aboutus.fact_1_number,
            "Факт 1 сан",
        )

        self.assertEqual(
            aboutus.fact_1_text,
            "Раз мы поднимались на вершины Тянь-Шаня с нашими туристами."
        )


        