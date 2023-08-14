from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Review


class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Review
    template_name = "reviews/create_review.html"
    fields = ["title", "satisfaction", "description", ]
    success_message = "Your review has been successfully added!"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
