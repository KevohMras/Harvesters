from django.contrib import admin
from .models import Product, Subscriber

admin.site.register(Product)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email", "subscribed_at")

admin.site.register(Subscriber, SubscriberAdmin)