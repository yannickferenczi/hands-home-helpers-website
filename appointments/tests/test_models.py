from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, time, datetime, timedelta

from appointments.models import Appointment
from tasks.models import Task


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test",
            password="test",
            email="test@test.com",
        )

        self.task = Task.objects.create(
            name="task test",
            owner=self.user,
        )

        self.appointment = Appointment.objects.create(
            appointment_owner=self.user,
            appointment_day=date(2025, 6, 21),
            appointment_start_time=time(10, 30),
            appointment_end_time=time(12),
        )

    def test_appointment_starting_time_as_date_time(self):
        self.assertEqual(
            self.appointment.starting_time_as_date_time,
            datetime(2025, 6, 21, 10, 30),
            )

    def test_appointment_ending_time_as_date_time(self):
        self.assertEqual(
            self.appointment.ending_time_as_date_time,
            datetime(2025, 6, 21, 12),
        )

    def test_appointment_duration(self):
        self.assertEqual(
            self.appointment.appointment_duration,
            90,
        )

    def test_appointment_has_minimum_time(self):
        self.assertTrue(self.appointment.has_minimum_time)
