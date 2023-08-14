from django.urls import path

from . import views

urlpatterns = [
    # path('', views.reviews, name="reviews"),
    path(
        'add_review/',
        views.ReviewCreateView.as_view(),
        name="review-add",
    ),
]
