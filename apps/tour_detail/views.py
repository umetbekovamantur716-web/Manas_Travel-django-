from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.turs.models import PopularTour
from .models import TourDetail, BookingRequest
from apps.contact.models import FooterContact


def tour_detail_view(request, tour_id):
    tour = get_object_or_404(PopularTour, id=tour_id)
    detail = getattr(tour, 'detail', None)
    footer_info = FooterContact.objects.last()
    
    # Брондлоо формасын кабыл алуу
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        people_count = request.POST.get('people_count', 1)
        date_str = request.POST.get('date')

        if name and phone:
            from datetime import datetime
            booking_date = None
            if date_str:
                try:
                    booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                except ValueError:
                    booking_date = None

            BookingRequest.objects.create(
                tour=tour,
                name=name,
                phone=phone,
                people_count=int(people_count) if people_count else 1,
                date=booking_date
            )
            messages.success(request, 'Рахмат! Ваша заявка на бронирование принята. Мы скоро свяжемся с вами.')
        return redirect('tour_detail', tour_id=tour.id)

    included_list = []
    not_included_list = []
    if detail:
        included_list = [line.strip() for line in detail.included.split('\n') if line.strip()]
        not_included_list = [line.strip() for line in detail.not_included.split('\n') if line.strip()]
    
    context = {
        'tour': tour,
        'detail': detail,
        'included_list': included_list,
        'not_included_list': not_included_list,
        'footer_info': footer_info,
    }
    return render(request, 'detailed.html', context)

