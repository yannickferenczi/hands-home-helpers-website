from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import View
from datetime import datetime, date, time, timedelta

from config.base_settings import OPENING_HOUR, CLOSING_HOUR
from .models import CustomHTMLCalendar, Appointment
from .forms import BookingForm


class CustomHTMLCalendarView(LoginRequiredMixin, View):
    """
    This class render a Monthly HTMLcalendar
    """

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
    """
    This function displays a form to create appointment.
    """
    selected_day = date(year, month, day)
    if selected_day.weekday() == 0:
        day_before = selected_day - timedelta(days=2)
    else:
        day_before = selected_day - timedelta(days=1)

    if selected_day.weekday() == 5:
        day_after = selected_day + timedelta(days=2)
    else:
        day_after = selected_day + timedelta(days=1)

    current_month = datetime.today().month
    daily_appointments = Appointment.objects.filter(
        appointment_day=selected_day
    )

    # check for every half-hour if it is already booked or not
    daily_schedule = []
    for i in range(OPENING_HOUR, CLOSING_HOUR):
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
            appointment_date = new_appointment.appointment_day
            list_of_tasks = new_appointment.appointment_tasks.all()
            for task in list_of_tasks:
                task.due_date = appointment_date
                task.save()
            a = "stop"
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


class AppointmentDetailView(LoginRequiredMixin, generic.DetailView):
    """
    This view render the detail of a selected appointment.
    """
    model = Appointment
    template_name = "appointments/appointment_detail.html"
    context_object_name = "appointment"


class AppointmentUpdateView(
        SuccessMessageMixin,
        LoginRequiredMixin,
        UpdateView):
    """
    This view display a form to update a selected appointment.
    """
    model = Appointment
    form_class = BookingForm
    template_name = "appointments/update_appointment.html"
    # fields = [
    #     "appointment_day",
    #     "appointment_start_time",
    #     "appointment_end_time",
    #     "appointment_tasks",
    # ]
    success_message = "Your appointment has been successfully updated!"

    def get_form_kwargs(self):
        """Passes the request object to the form class."""
        kwargs = super(AppointmentUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class AppointmentDeleteView(
        SuccessMessageMixin,
        LoginRequiredMixin,
        DeleteView):
    """
    This view leads through the deletion process of a selected appointment.
    """
    model = Appointment
    template_name = "appointments/delete_appointment.html"
    success_url = reverse_lazy("dashboard")
    success_message = "Your appointment has been successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AppointmentDeleteView, self).delete(
            request,
            *args,
            **kwargs,
        )
