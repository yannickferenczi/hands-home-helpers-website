from calendar import HTMLCalendar
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime, time
from math import floor

from tasks.models import Task


class Appointment(models.Model):
    """
    This class creates a table to save Appointment instances in the database.
    """
    POSSIBLE_TIME = [
        (time.fromisoformat("07:00"), "7:00"),
        (time.fromisoformat("07:30"), "7:30"),
        (time.fromisoformat("08:00"), "8:00"),
        (time.fromisoformat("08:30"), "8:30"),
        (time.fromisoformat("09:00"), "9:00"),
        (time.fromisoformat("09:30"), "9:30"),
        (time.fromisoformat("10:00"), "10:00"),
        (time.fromisoformat("10:30"), "10:30"),
        (time.fromisoformat("11:00"), "11:00"),
        (time.fromisoformat("11:30"), "11:30"),
        (time.fromisoformat("12:00"), "12:00"),
        (time.fromisoformat("12:30"), "12:30"),
        (time.fromisoformat("13:00"), "13:00"),
        (time.fromisoformat("13:30"), "13:30"),
        (time.fromisoformat("14:00"), "14:00"),
        (time.fromisoformat("14:30"), "14:30"),
        (time.fromisoformat("15:00"), "15:00"),
        (time.fromisoformat("15:30"), "15:30"),
        (time.fromisoformat("16:00"), "16:00"),
        (time.fromisoformat("16:30"), "16:30"),
        (time.fromisoformat("17:00"), "17:00"),
        (time.fromisoformat("17:30"), "17:30"),
        (time.fromisoformat("18:00"), "18:00"),
        (time.fromisoformat("18:30"), "18:30"),
        (time.fromisoformat("19:00"), "19:00"),
    ]
    appointment_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="appointment_owner",
    )
    appointment_day = models.DateField(verbose_name="Day of appointment")
    appointment_start_time = models.TimeField(
        choices=POSSIBLE_TIME, verbose_name="Starting time")
    appointment_end_time = models.TimeField(
        choices=POSSIBLE_TIME,
        verbose_name="Ending time"
    )
    appointment_tasks = models.ManyToManyField(
        Task,
        related_name="associated_tasks",
    )

    def __str__(self):
        return f"{self.appointment_day}"

    @property
    def starting_time_as_date_time(self):
        return datetime.combine(
            self.appointment_day, self.appointment_start_time)

    @property
    def ending_time_as_date_time(self):
        return datetime.combine(
            self.appointment_day, self.appointment_end_time)

    @property
    def appointment_duration(self):
        return floor(
            (self.ending_time_as_date_time - self.starting_time_as_date_time)
            .total_seconds() / 3600)

    def get_absolute_url(self):
        return reverse('dashboard')

    # ---------------------------------------------
    # THE FOLLOWING FUNCTION HAS BEEN IMPORTED AND ONLY A LITTLE BIT MODIFIED
    # MORE DETAILS IN THE CREDITS SECTION OF THE README.md FILE
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:
            overlap = False
        elif ((new_start >= fixed_start and new_start <= fixed_end)
                or (new_end >= fixed_start and new_end <= fixed_end)):
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:
            overlap = True
        return overlap

    def has_minimum_time(self):
        return timedelta((self.ending_time_as_date_time - self.starting_time_as_date_time).total_seconds() / 60) >= timedelta(minutes=60)

    # ---------------------------------------------
    # THE FOLLOWING FUNCTION HAS BEEN IMPORTED AND ONLY A LITTLE BIT MODIFIED
    # MORE DETAILS IN THE CREDITS SECTION OF THE README.md FILE
    def clean(self):
        if self.ending_time_as_date_time <= self.starting_time_as_date_time:
            raise ValidationError('Ending time must be after starting time')

        appointments = Appointment.objects.filter(
            appointment_day=self.appointment_day)
        if appointments.exists():
            for appointment in appointments:
                if appointment.pk == self.pk:
                    continue
                if self.check_overlap(
                    appointment.appointment_start_time,
                    appointment.appointment_end_time,
                    self.appointment_start_time,
                    self.appointment_end_time,
                ):
                    raise ValidationError(
                        'There is an overlap with another appointment: '
                        + str(appointment.appointment_day) + ', '
                        + str(appointment.appointment_start_time) + '-'
                        + str(appointment.appointment_end_time)
                    )

        if not self.has_minimum_time():
            raise ValidationError('You cannot schedule less than 1 hour.')

# ---------------------------------------------
# THE FOLLOWING CLASS HAS BEEN IMPORTED AND ONLY A LITTLE BIT MODIFIED
# MORE DETAILS IN THE CREDITS SECTION OF THE README.md FILE
class CustomHTMLCalendar(HTMLCalendar):
    """
    This class creates an html calendar.
    
    Each upcoming day is a link to a daily view of the calendar.
    """

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        cssclass = self.cssclasses[weekday]
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            selected_date = date(self._year, self._month, day)
            cssclass += f" day-{day}"
            if weekday == 6:
                # it is Sunday
                return f'<td class="{cssclass}">{day}</td>'
            if selected_date <= date.today():
                if date.today() == selected_date:
                    cssclass += ' today'
                cssclass += ' past-day'
                return f'<td class="{cssclass}">{day}</td>'
            else:
                daily_appointments = Appointment.objects.filter(
                    appointment_day=selected_date)
                total_daily_booking = sum(
                    [appointment.appointment_duration
                     for appointment in daily_appointments]
                )
                if total_daily_booking >= 10:
                    cssclass += ' fully-booked'
                elif total_daily_booking >= 6:
                    cssclass += ' low-availability'
                else:
                    cssclass += ' high-availability'

            return f'<td class="{cssclass}">'\
                f'{self._get_day_link(self._year, self._month, day)}</td>'

    def formatmonth(
            self,
            theyear: int,
            themonth: int,
            withyear: bool = ...) -> str:
        self._year = theyear
        self._month = themonth
        self.cssclass_month += ' dashboard-item'
        return super().formatmonth(theyear, themonth, withyear)

    def _get_day_link(self, year, month, day_number):
        return f'<a href="/appointments/dailycalendar/{year}/'\
            f'{month}/{day_number}/">{day_number}</a>'
