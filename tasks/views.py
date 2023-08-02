from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "tasks/dashboard.html"
    paginated_by = 50

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
