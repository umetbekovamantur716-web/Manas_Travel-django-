from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.turs.urls')), 
    path('tour/', include('apps.tour_detail.urls')),
    path('contact/', include('apps.contact.urls')),
    path('about/', include('apps.about.urls')),
    path('gallery/', include('apps.gallery.urls')),
]

# Медиа файлдар (development учурда)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
