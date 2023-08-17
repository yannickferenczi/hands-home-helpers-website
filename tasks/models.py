from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Employee(models.Model):
    """
    This class creates a table to save Employee instances in the database.
    """
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    """
    This class creates a table to save Task instances in the database.
    """
    CATEGORIES = [
        ("Gardening", "Gardening"),
        ("Cleaning", "Cleaning"),
        ("Garden patch", "Garden patch"),
        ("Swimming pool", "Swimming pool"),
        ("Renovation and repair", "Renovation and repair"),
        ("Home care", "Home care"),
    ]

    name = models.CharField(max_length=250, verbose_name="Description")
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="task_owner",
    )
    created_on = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        default="CLEANING",
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name="employees",
        blank=True,
        null=True,
    )
    comment = models.CharField(max_length=250, blank=True, null=True)
    due_date = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dashboard")
