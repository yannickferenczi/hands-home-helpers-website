from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.TaskList.as_view(),
        name="dashboard"
    ),
    path(
        'add_task/',
        views.TaskCreateView.as_view(),
        name="add_task"
    ),
    path(
        'task_detail/<int:pk>/',
        views.TaskDetailView.as_view(),
        name="task_detail"
    ),
    path(
        'update_task/<int:pk>/',
        views.TaskUpdateView.as_view(),
        name="update_task"
    ),
    path(
        'delete_task/<int:pk>/',
        views.TaskDeleteView.as_view(),
        name="delete_task"
    ),
]
