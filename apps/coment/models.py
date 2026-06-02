from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Колдонуучунун аты")
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Баасы")
    text = models.TextField(verbose_name="Пикир / Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Кошулган убактысы")

    class Meta:
        verbose_name = "Пикир"
        verbose_name_plural = "Пикирлер"
        ordering = ['-created_at'] # Жаңы жазылган пикирлер эң өйдө турат

    def __str__(self):
        return f"{self.name} - {self.stars} ★"