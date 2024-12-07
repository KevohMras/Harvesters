from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Product

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def products(request):
    return render(request, "products.html")

def contact(request):
    return render(request, "contact.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send an email notification
        send_mail(
            f'New Contact Message from {name}',
            f'Message: {message}\n\nEmail: {email}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # Replace with your email
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")

def products(request):
    product_list = Product.objects.all()
    return render(request, "products.html", {'products': product_list})
