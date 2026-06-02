from django.contrib import admin
from .models import TravelSlider, PopularTour

@admin.register(TravelSlider)
class TravelSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge', 'price', 'is_active')


@admin.register(PopularTour)
class PopularTourAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration',)
    list_filter = ('is_popular',)
