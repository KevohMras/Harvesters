from django.contrib import admin
from .models import Product,Subscriber


admin.site.register(Product)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email" ,"subscribed_at")

