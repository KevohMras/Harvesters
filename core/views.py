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

def contact(request):
    return render(request, "contact.html")


def contact_view(request):
    if request.method == "POST":
        # Debug: Print request.POST data to confirm form submission
        print(request.POST)

        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Debug: Confirm data is being captured
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)

        # Save the data to the database
        if name and email and subject and message:  # Basic validation
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            print("Data saved successfully")
            return redirect('success_page')  # Redirect after successful save

    return render(request, 'contact.html')

# def contact_view(request):
#     if request.method == "POST":
#         name = request.POST.get('name')  # Extract the 'name' field
#         email = request.POST.get('email')  # Extract the 'email' field
#         subject = request.POST.get('subject')  # Extract the 'subject' field
#         message = request.POST.get('message')  # Extract the 'message' field
#
#         # Save the data to the database
#         Contact.objects.create(name=name, email=email, subject=subject, message=message)
#
#         return redirect('success_page')  # Redirect to success page after submission
#
#     return render(request, 'contact.html')  # Render the contact form page

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#         # Send an email notification
#         send_mail(
#             f'New Contact Message from {name}',
#             f'Message: {message}\n\nEmail: {email}',
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.DEFAULT_FROM_EMAIL],  # Replace with your email
#         )
#
#         return render(request, "contact.html", {"success": True})
#
#     return render(request, "contact.html")

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

