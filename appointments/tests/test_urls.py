from django.test import SimpleTestCase
from django.urls import reverse, resolve

from appointments import views


class TestUrls(SimpleTestCase):

    def test_calendar_url_is_resolves(self):
        url = reverse('calendar', args=[8])
        self.assertEquals(
            resolve(url).func.view_class,
            views.CustomHTMLCalendarView,
        )

    def test_dailycalendar_url_is_resolves(self):
        url = reverse('dailycalendar', args=[2023, 8, 18])
        self.assertEquals(resolve(url).func, views.booking)

    def test_appointment_detail_url_is_resolves(self):
        url = reverse('appointment_detail', args=[1])
        self.assertEquals(
            resolve(url).func.view_class,
            views.AppointmentDetailView,
        )

    def test_update_appointment_url_is_resolves(self):
        url = reverse('update_appointment', args=[1])
        self.assertEquals(
            resolve(url).func.view_class,
            views.AppointmentUpdateView,
        )

    def test_delete_appointment_url_is_resolves(self):
        url = reverse('delete_appointment', args=[1])
        self.assertEquals(
            resolve(url).func.view_class,
            views.AppointmentDeleteView,
        )
