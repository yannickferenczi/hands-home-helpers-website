from django.contrib import admin
from django.urls import path, include

from .views import index, about

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('administration_panel/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('contact/', include('contact.urls')),
    path('dashboard/', include('tasks.urls')),
    path('offers/', include('offers.urls')),
    path('appointments/', include('appointments.urls')),
    path('reviews/', include('reviews.urls')),
]
