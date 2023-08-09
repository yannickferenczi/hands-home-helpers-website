from django.db import models
from math import floor
from cloudinary.models import CloudinaryField


class Offer(models.Model):
    """
    This class creates new Offer instances
    """
    title = models.CharField(max_length=250)
    featured_image = CloudinaryField("image")
    hours = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=4, decimal_places=2)
    equipment_included = models.BooleanField(default=False)
    cleaning_product_included = models.BooleanField(default=False)
    deferrable_hours = models.BooleanField(default=False)
    minimum_duration = models.IntegerField()
    minimum_time_cancelation = models.IntegerField()

    class Meta:
        ordering = ["hours"]

    def __str__(self):
        return self.title

    @property
    def total_price(self):
        return floor(price_per_hour * hours)
