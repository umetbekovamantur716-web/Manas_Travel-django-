from django.contrib import admin
from .models import FooterContact, ContactPage, ContactRequest


@admin.register(FooterContact)
class FooterContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address', 'work_hours')


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address', 'work_hours')
    fieldsets = (
        ('Негизги маалыматтар', {
            'fields': ('phone', 'email', 'address', 'work_hours')
        }),
        ('Карта', {
            'fields': ('map_iframe_url',)
        }),
        ('Социалдык тармактар', {
            'fields': ('instagram_url', 'telegram_url', 'facebook_url', 'vk_url'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone', 'message')
    list_editable = ('is_processed',)
    readonly_fields = ('created_at',)