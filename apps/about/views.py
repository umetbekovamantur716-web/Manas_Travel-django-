from django.shortcuts import render
from .models import AboutUs
from apps.contact.models import FooterContact
from apps.gallery.models import GalleryImage


def about_view(request):
    about_info = AboutUs.objects.last()
    footer_info = FooterContact.objects.last()
    gallery_images = GalleryImage.objects.filter(is_active=True)[:8]  # 8 сүрөткө чейин
    return render(request, 'kampany.html', {
        'about_info': about_info,
        'footer_info': footer_info,
        'gallery_images': gallery_images,
    })                   