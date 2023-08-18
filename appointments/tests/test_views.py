from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from datetime import date, time

from appointments.models import Appointment
from appointments.views import CustomHTMLCalendarView, AppointmentDetailView


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test",
            password="test",
            email="test@test.com",
        )
        self.appointment = Appointment.objects.create(
            appointment_owner=self.user,
            appointment_day=date(2025, 6, 21),
            appointment_start_time=time(10, 30),
            appointment_end_time=time(12),
        )

    def test_CustomHTMLCalendarView_get(self):
        self.calendar_url = reverse('calendar', args=[8])
        self.client.login(username='test', password='test')
        response = self.client.get(self.calendar_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/calendar.html')

    def test_AppointmentDetailView_get(self):
        self.detail_url = reverse('appointment_detail', args=[1])
        self.client.login(username='test', password='test')
        response = self.client.get(self.detail_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'appointments/appointment_detail.html',
        )
