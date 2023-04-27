from django.db import models
from users.models import Profile
from dropoff_locator.models import Site
from django.utils import timezone


class Request(models.Model):
    STATUS = [
        ("Open", "Open"),
        ("Completed", "Completed"),
        ("Canceled", "Canceled"),
    ]
    donor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)


class Message(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)
