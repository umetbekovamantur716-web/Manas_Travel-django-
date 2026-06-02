from django.contrib import admin
from .models import TourDetail, BookingRequest


@admin.register(TourDetail)
class TourDetailAdmin(admin.ModelAdmin):
    list_display = ['tour', 'location', 'max_people', 'price_per_person', 'is_active']
    list_filter = ['is_active']
    search_fields = ['tour__title', 'location']


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'tour', 'people_count', 'date', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at', 'tour']
    search_fields = ['name', 'phone', 'tour__title']
    list_editable = ['is_processed']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

