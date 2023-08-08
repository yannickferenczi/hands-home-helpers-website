from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """This function render the contact form"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your form has been successfully submitted!",
            )
            return redirect("home")
    else:
        form = ContactForm()
        return render(request, "contact/contact.html", {"form": form})
