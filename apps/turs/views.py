from django.shortcuts import render, redirect
from .models import TravelSlider, PopularTour
from apps.coment.models import Review
from django.db.models import Q 
from apps.about.models import AboutUs
from apps.contact.models import FooterContact


def get_footer_info():
    return FooterContact.objects.last()


def home_page(request):
    # Форма жөнөтүлсө (POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        stars = request.POST.get('stars')
        text = request.POST.get('text')
        if name and stars and text:
            Review.objects.create(name=name, stars=stars, text=text)
        return redirect('home')

    slides = TravelSlider.objects.filter(is_active=True)
    tours = PopularTour.objects.filter(is_popular=True)
    reviews = Review.objects.all()
    reviews_count = Review.objects.count()
    about_info = AboutUs.objects.last() 
    footer_info = get_footer_info()

    return render(request, 'index.html', {
        'slides': slides,
        'tours': tours,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'about_info': about_info,
        'footer_info': footer_info,
    })


def turs_home(request):
    tours = PopularTour.objects.all()
    footer_info = get_footer_info()
    
    return render(request, 'turs.html', {
        'tours': tours,
        'footer_info': footer_info,
    })


def search_tours_view(request):
    query = request.GET.get('search', '')
    
    if query:
        results = PopularTour.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(duration__icontains=query)
        )
    else:
        results = PopularTour.objects.all() 

    reviews = Review.objects.all()[:2]
    reviews_count = Review.objects.count()
    footer_info = get_footer_info()
    
    context = {
        'search_results': results,
        'query': query,
        'is_search': True,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'footer_info': footer_info,
    }
    return render(request, 'index.html', context)