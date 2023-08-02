from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name="dashboard"),
    path('detail_task/<int:pk>/', views.TaskDetailView.as_view(), name="task_detail"),
]
