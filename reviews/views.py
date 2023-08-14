from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Review


class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    This class creates a Review instance.

    Users must be logged into their personal account to access this content.
    """

    model = Review
    template_name = "reviews/create_review.html"
    fields = ["title", "satisfaction", "description", ]
    success_message = "Your review has been successfully added!"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class ReviewUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    This class update the selected Review instance.

    Users must be logged into their personal account to access this content.
    """

    model = Review
    template_name = "reviews/update_review.html"
    fields = ["title", "satisfaction", "description", ]
    success_message = "Your review has been successfully updated!"


class ReviewDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """
    This class delete the selected Review instance.

    Users must be logged into their personal account to access this content.
    """

    model = Review
    template_name = "reviews/delete_review.html"
    success_url = reverse_lazy("dashboard")
    success_message = "Your review has been successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReviewDeleteView, self).delete(
            request,
            *args,
            **kwargs,
        )
