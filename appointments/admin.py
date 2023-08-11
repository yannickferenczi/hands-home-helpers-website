from django.contrib import admin
from django import forms

from .models import Appointment

from .forms import BookingForm
from tasks.models import Task


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """
    This class displays instances of the Appointment model in the admin panel
    """
    list_display = (
        "appointment_owner",
        "appointment_day",
        "appointment_start_time",
        "appointment_end_time",
    )
    list_display_links = ("appointment_owner", )
    list_filter = ("appointment_day", )
    ordering = ["appointment_day", "appointment_start_time"]
    readonly_fields = ["appointment_owner", ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "appointment_tasks":
            kwargs["queryset"] = Task.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        owner = obj.appointment_owner
        form.base_fields['appointment_tasks'].queryset = Task.objects.filter(
            owner=owner
        )
        return form
