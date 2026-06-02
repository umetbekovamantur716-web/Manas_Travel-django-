from django.test import TestCase
from apps.gallery.models import GalleryImage


class GalleryImageTestCase(TestCase):
    def test_galleryimage_create(self):
        galleryimage = GalleryImage.objects.create(
            title = "text",
            image = "test_image.gif",
            order = 89,
            is_active = True,
            created_at = 2026
        )

        self.assertEqual(galleryimage.title,"text")
        self.assertEqual(galleryimage.image,"test_image.gif")
        self.assertEqual(galleryimage.order, 89)
        self.assertEqual(galleryimage.is_active, True)
        self.assertEqual(galleryimage.created_at.year, 2026)
        