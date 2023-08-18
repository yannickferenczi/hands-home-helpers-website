from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from datetime import datetime

from .models import Task
from appointments.models import Appointment


class TaskList(LoginRequiredMixin, generic.ListView):
    """
    This class display the Task instances owned by the logged in user.

    Users must be logged into their personal account to access this content.
    """

    model = Task
    template_name = "tasks/dashboard.html"
    paginated_by = 50

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.filter(
            appointment_owner=self.request.user
        ).order_by("appointment_day")
        context["appointments"] = appointments
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    """
    This class display details of the selected Task instance.

    Users must be logged into their personal account to access this content.
    """

    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    This class creates a Task instance.

    Users must be logged into their personal account to access this content.
    """

    model = Task
    template_name = "tasks/create_task.html"
    fields = ["name", "category", ]
    success_message = "Your task has been successfully added!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    This class update the selected Task instance.

    Users must be logged into their personal account to access this content.
    """

    model = Task
    template_name = "tasks/update_task.html"
    fields = ["name", "category", ]
    success_message = "Your task has been successfully updated!"


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """
    This class delete the selected Task instance.

    Users must be logged into their personal account to access this content.
    """

    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("dashboard")
    success_message = "Your task has been successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDeleteView, self).delete(request, *args, **kwargs)
