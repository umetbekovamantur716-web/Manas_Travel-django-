from django.db import models


class GalleryImage(models.Model):
    """Галерея сүрөттөрү"""
    title = models.CharField(max_length=100, verbose_name="Аталышы", blank=True)
    image = models.ImageField(upload_to='gallery/', verbose_name="Сүрөт")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")
    is_active = models.BooleanField(default=True, verbose_name="Активдүү")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Галерея сүрөтү"
        verbose_name_plural = "Галерея сүрөттөрү"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title or f"Сүрөт #{self.id}"
