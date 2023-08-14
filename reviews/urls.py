from django.urls import path

from . import views

urlpatterns = [
    path(
        'add_review/',
        views.ReviewCreateView.as_view(),
        name="add_review",
    ),
    path(
        'update_review/<int:pk>/',
        views.ReviewUpdateView.as_view(),
        name="update_review",
    ),
    path(
        'delete_review/<int:pk>/',
        views.ReviewDeleteView.as_view(),
        name="delete_review",
    ),
]
