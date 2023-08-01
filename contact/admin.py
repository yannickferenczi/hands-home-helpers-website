from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "answered",
        "email",
        "subject",
    )

    list_display_links = ["email", ]

    list_filter = ["answered", "subject",]

    list_editable = ["answered", ]
