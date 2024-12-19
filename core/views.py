from django.shortcuts import redirect,render
# from django.core.mail import send_mail
# from django.conf import settings
from django.contrib import messages

from .models import Product
from .models import Subscriber
from .models import Contact

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def products(request):
    return render(request, "products.html")

def contactform(request):
    return render(request, "contact.html")

def contact(request):
    if request.method == "POST":
        # Extract form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate data and save it to the database
        if name and email and subject and message:  # Basic validation to ensure no field is empty
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # Add a success message
            messages.success(request, "Your message has been sent successfully!")
        else:
            # Add an error message
            messages.error(request, "All fields are required. Please fill out the form correctly.")

    # Render the contact form template
    return render(request, 'contact.html')

def products(request):
    product_list = Product.objects.all()
    return render(request, "products.html", {'products': product_list})

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, "You are already subscribed!")
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing!")
        else:
            messages.error(request, "Please enter a valid email address!")
    return redirect("/")

