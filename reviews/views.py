from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Review


# def reviews(request):
#     tasks = Task.objects.all()
#     reviews = Review.objects.all()
#     # filter(online=True).order_by(["created_on"])
#     range_full_stars = {}
#     range_empty_stars = {}
#     for review in reviews:
#         range_full_stars[review.id] = range(review.satisfaction)
#         range_empty_stars[review.id] = range(5 - review.satisfaction)
#     return render(
#         request,
#         "reviews/reviews_list.html",
#         {"reviews": reviews, "tasks": tasks},
#     )


class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Review
    template_name = "reviews/create_review.html"
    fields = ["title", "satisfaction", "description", ]
    success_message = "Your review has been successfully added!"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
