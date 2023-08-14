from django.urls import path

from . import views

urlpatterns = [
    path(
        'calendar/<int:month>/',
        views.CustomHTMLCalendarView.as_view(),
        name="calendar",
    ),
    path(
        'dailycalendar/<int:year>/<int:month>/<int:day>/',
        views.booking,
        name="dailycalendar",
    ),
    path(
        'appointment_detail/<int:pk>',
        views.AppointmentDetailView.as_view(),
        name="appointment_detail",
    ),
    path(
        'update_appointment/<int:pk>',
        views.AppointmentUpdateView.as_view(),
        name="update_appointment",
    ),
    path(
        'delete_appointment/<int:pk>',
        views.AppointmentDeleteView.as_view(),
        name="delete_appointment",
    ),
]
