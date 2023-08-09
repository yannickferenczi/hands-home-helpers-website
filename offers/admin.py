from django.contrib import admin

from .models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """
    This class displays instances of the Offer model in the admin panel
    """
    list_display = ['title', "hours", "price_per_hour", ]
    ordering = ['hours']
