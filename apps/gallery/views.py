from django.shortcuts import render
from apps.gallery.models import GalleryImage


def gallery_list(request):
    images = GalleryImage.objects.filter(is_active=True)
    return render(request, 'gallery.html', {
        'images': images,
    })
