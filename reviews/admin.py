from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "satisfaction",
        "online",
        "answered",
        "user",
    )
    list_filter = ("online", "answered", )
