from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import View
from datetime import datetime, date, time, timedelta

from .models import CustomHTMLCalendar, Appointment
from .forms import BookingForm


class CustomHTMLCalendarView(LoginRequiredMixin, View):
    def get(self, request, month, *args, **kwargs):
        current_year = datetime.now().year
        cal = CustomHTMLCalendar().formatmonth(current_year, month)
        return render(
            request,
            "appointments/calendar.html",
            {"cal": cal, "current_month": month}
        )


@login_required
def booking(request, year, month, day):
    selected_day = date(year, month, day)
    day_before = selected_day - timedelta(days=1)
    day_after = selected_day + timedelta(days=1)
    current_month = datetime.today().month
    daily_appointments = Appointment.objects.filter(
        appointment_day=selected_day
    )

    # check for every half-hour if it is already booked or not
    daily_schedule = []
    for i in range(7, 19):
        hourly_schedule = [False, False]
        datetime_to_check_1 = datetime.combine(
            selected_day,
            time(hour=i)
        ) + timedelta(minutes=15)
        datetime_to_check_2 = datetime.combine(
            selected_day,
            time(hour=i)
        ) + timedelta(minutes=45)
        for appointment in daily_appointments:
            if (appointment.starting_time_as_date_time
                    < datetime_to_check_1
                    < appointment.ending_time_as_date_time):
                hourly_schedule[0] = True
            if (appointment.starting_time_as_date_time
                    < datetime_to_check_2
                    < appointment.ending_time_as_date_time):
                hourly_schedule[1] = True
        daily_schedule.append(hourly_schedule)

    if request.method == "POST":
        query = request.POST.copy()
        query["appointment_day"] = selected_day
        form = BookingForm(
            query,
            request=request,
        )
        if form.is_valid():
            new_appointment = form.save(commit=False)
            new_appointment.appointment_owner = request.user
            new_appointment.save()
            form.save_m2m()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your appointment has been successfully created!",
            )
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = BookingForm(request=request)
    return render(
        request,
        "appointments/dailycalendar.html",
        {
            "selected_day": selected_day,
            "day_before": day_before,
            "day_after": day_after,
            "current_month": current_month,
            "daily_schedule": daily_schedule,
            "form": form,
        },
    )