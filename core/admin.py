from django.contrib import admin
from .models import Product, Subscriber, Contact

admin.site.register(Product)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email", "subscribed_at")

admin.site.register(Subscriber, SubscriberAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # Columns to display
    search_fields = ('name', 'email', 'subject', 'created_at')  # Search functionality
    list_filter = ('name', 'email', 'subject','created_at',)  # Filter by date

admin.site.register(Contact, ContactAdmin)

