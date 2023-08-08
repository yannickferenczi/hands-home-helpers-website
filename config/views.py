from django.shortcuts import render


def index(request):
    """This function render the landing page of the project."""
    return render(request, "index.html")


def about(request):
    """This function render the about page of the project."""
    return render(request, "about.html")
