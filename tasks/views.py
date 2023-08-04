from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Task


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "tasks/dashboard.html"
    paginated_by = 50

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    template_name = "tasks/create_task.html"
    fields = ["name", "repeat", "category", ]
    success_message = "Your task has been successfully added!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "tasks/update_task.html"
    fields = ["name", "repeat", "category", ]
    success_message = "Your task has been successfully updated!"


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("dashboard")
    success_message = "Your task has been successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDeleteView, self).delete(request, *args, **kwargs)
