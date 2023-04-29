from django.db import models
from users.models import Profile
from dropoff_locator.models import Site
from django.utils import timezone


class Request(models.Model):
    STATUS = [
        ("Sent", "Sent"),  # messages not yet read by host
        ("OpenNotScheduled", "OpenNotScheduled"),
        ("Scheduled", "Scheduled"),
        ("Rejected", "Rejected"),
        ("Completed", "Completed"),
        ("Canceled", "Canceled"),
    ]
    donor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, unique=False, related_name="requests"
    )
    host = models.ForeignKey(
        Profile, on_delete=models.CASCADE, unique=False, related_name="receives"
    )
    site = models.ForeignKey(Site, on_delete=models.CASCADE, unique=False)
    status = models.CharField(max_length=25, choices=STATUS, default="Sent")


class Message(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)
