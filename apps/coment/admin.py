from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'created_at')
    list_filter = ('stars', 'created_at')
    search_fields = ('name', 'text')