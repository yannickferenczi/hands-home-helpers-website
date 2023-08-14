from django.shortcuts import render

from reviews.models import Review


def index(request):
    """This function render the landing page of the project."""
    reviews = Review.objects.filter(online=True).order_by("created_on")
    range_full_stars = {}
    range_empty_stars = {}
    for review in reviews:
        range_full_stars[review.id] = range(int(review.satisfaction))
        range_empty_stars[review.id] = range(5 - int(review.satisfaction))
    return render(request, "index.html", {"reviews": reviews})


def about(request):
    """This function render the about page of the project."""
    return render(request, "about.html")
