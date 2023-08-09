from django.shortcuts import render
from django.views.generic import ListView

from .models import Offer


class OffersListView(ListView):
    """
    This class display the Offer instances.
    """
    model = Offer
    template_name = "offers/offers.html"
    context_object_name = "offers"
