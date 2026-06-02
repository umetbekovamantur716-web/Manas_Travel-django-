from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FooterContact, ContactPage, ContactRequest


def contact_view(request):
    # Форма жөнөтүлсө
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if name and phone:
            ContactRequest.objects.create(name=name, phone=phone, message=message)
            messages.success(request, 'Рахмат! Ваша заявка принята. Мы свяжемся с вами в ближайшее время.')
        return redirect('contact')

    footer_info = FooterContact.objects.last()
    contact_info = ContactPage.objects.last()
    return render(request, 'contact.html', {
        'footer_info': footer_info,
        'contact_info': contact_info,
    })
