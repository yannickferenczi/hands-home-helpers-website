from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Review(models.Model):
    RATING = [
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    ]
    title = models.CharField(max_length=250, )
    satisfaction = models.CharField(
        max_length=1,
        choices=RATING,
        default="5",
    )
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    online = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review_owner",
    )

    def __str__(self):
        return f"{self.title} from {self.user.username}"

    def filled_satisfaction_stars(self):
        return range(int(self.satisfaction))

    def empty_satisfaction_stars(self):
        return range(5 - int(self.satisfaction))

    def get_absolute_url(self):
        return reverse("dashboard")
