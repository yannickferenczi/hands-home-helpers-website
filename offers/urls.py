from django.urls import path

from . import views


urlpatterns = [
    path('', views.OffersListView.as_view(), name="offers"),
]
