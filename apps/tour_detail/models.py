from django.db import models
from apps.turs.models import PopularTour


class TourDetail(models.Model):
    tour = models.OneToOneField(PopularTour, on_delete=models.CASCADE, related_name='detail', verbose_name='Тур')
    full_description = models.TextField(verbose_name='Толук описание')
    location = models.CharField(max_length=200, verbose_name='Локация')
    max_people = models.PositiveIntegerField(default=12, verbose_name='Максималдуу адам саны')
    
    # Программа — күнүмдүк
    day1_title = models.CharField(max_length=200, verbose_name='1-күн аталышы')
    day1_desc = models.TextField(verbose_name='1-күн описание')
    day2_title = models.CharField(max_length=200, blank=True, verbose_name='2-күн аталышы')
    day2_desc = models.TextField(blank=True, verbose_name='2-күн описание')
    day3_title = models.CharField(max_length=200, blank=True, verbose_name='3-күн аталышы')
    day3_desc = models.TextField(blank=True, verbose_name='3-күн описание')
    
    # Эмне кирет / кирбейт
    included = models.TextField(verbose_name='Эмнелер кирет')
    not_included = models.TextField(verbose_name='Эмнелер кирбейт ')
    
    # Галерея сүрөттөрү
    gallery_image1 = models.ImageField(upload_to='tour_gallery/', blank=True, verbose_name='Галерея сүрөтү 1')
    gallery_image2 = models.ImageField(upload_to='tour_gallery/', blank=True, verbose_name='Галерея сүрөтү 2')
    gallery_image3 = models.ImageField(upload_to='tour_gallery/', blank=True, verbose_name='Галерея сүрөтү 3')
    
    # Брондоо үчүн
    price_per_person = models.PositiveIntegerField(default=0, verbose_name='Баасы (сом/киши)')
    
    is_active = models.BooleanField(default=True, verbose_name='Активдүү') 
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Турдун деталдары'
        verbose_name_plural = 'Турдун деталдары'
    
    def __str__(self):
        return f"{self.tour.title} - деталдары"


class BookingRequest(models.Model):
    """Тур брондлоо заявкалары"""
    tour = models.ForeignKey(PopularTour, on_delete=models.CASCADE, related_name='bookings', verbose_name='Тур')
    name = models.CharField(max_length=100, verbose_name='Аты-жөнү')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    people_count = models.PositiveIntegerField(default=1, verbose_name='Адам саны')
    date = models.DateField(blank=True, null=True, verbose_name='Каалаган дата')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_processed = models.BooleanField(default=False, verbose_name='Иштетилди')

    class Meta:
        verbose_name = 'Брондлоо заявкасы'
        verbose_name_plural = 'Брондлоо заявкалары'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.tour.title} ({self.phone})"
