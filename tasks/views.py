from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/create_task.html"
    fields = ["name", "repeat", "category", ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
