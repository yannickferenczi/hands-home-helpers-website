from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
