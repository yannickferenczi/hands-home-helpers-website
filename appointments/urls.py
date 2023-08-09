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
]
