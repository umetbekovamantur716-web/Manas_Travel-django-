from django.db import models

class TravelSlider(models.Model):
    badge = models.CharField(max_length=100, verbose_name="Акция тексти")
    title = models.CharField(max_length=200, verbose_name="Турдун аты")
    description = models.TextField(verbose_name="Кыскача түшүндүрмө")
    price = models.IntegerField(verbose_name="Баасы ($ менен)")
    image_url = models.URLField(verbose_name="Сүрөттүн шилтемеси (URL)", max_length=500)
    is_active = models.BooleanField(default=True, verbose_name="Активдүүбү?")

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайддар"

    def __str__(self):
        return self.title
    
    
class PopularTour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Турдун аты")
    duration = models.CharField(max_length=100, verbose_name="Убактысы (мис: 3 күн / 2 түн)")
    description = models.TextField(verbose_name="Кыскача түшүндүрмө")
    price = models.IntegerField(verbose_name="Баасы (сом менен)")
    image = models.ImageField(upload_to='tour_images/', verbose_name="Турдун сүрөтү")
    is_popular = models.BooleanField(default=True, verbose_name="Популярдуу тур катары көрсөтүлсүнбү?")

    class Meta:
        verbose_name = "Популярдуу тур"
        verbose_name_plural = "Популярдуу турлар"

    def __str__(self):
        return self.title
    
    