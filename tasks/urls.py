from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name="dashboard"),
    path('add_task/', views.TaskCreateView.as_view(), name="task_create"),
    path(
        'detail_task/<int:pk>/',
        views.TaskDetailView.as_view(),
        name="task_detail"
    ),
]
