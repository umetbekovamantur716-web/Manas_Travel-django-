from django.contrib import admin
from .models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'stat_clients', 'stat_tours', 'stat_experience')

    fieldsets = (
        ('Негизги маалымат', {
            'fields': ('title', 'description')
        }),
        ('Статистика', {
            'fields': ('stat_clients', 'stat_tours', 'stat_experience')
        }),
        ('Fun Facts (Фактылар)', {
            'fields': (
                ('fact_1_icon', 'fact_1_number', 'fact_1_text'),
                ('fact_2_icon', 'fact_2_number', 'fact_2_text'),
                ('fact_3_icon', 'fact_3_number', 'fact_3_text'),
                ('fact_4_icon', 'fact_4_number', 'fact_4_text'),
            )
        }),
        ('Принциптер', {
            'fields': (
                ('principle_1_title', 'principle_1_desc'),
                ('principle_2_title', 'principle_2_desc'),
            )
        }),
        ('Карта', {
            'fields': ('map_iframe_url',)
        }),
    )