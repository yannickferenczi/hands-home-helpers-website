from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()
        return render(request, "contact/contact.html", {"form": form})