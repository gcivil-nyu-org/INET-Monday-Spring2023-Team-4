from django.db import models


class dashboard(models.Model):
    borough = models.CharField(max_length=50)
    ntaname = models.CharField(max_length=50)
    sitename = models.CharField(max_length=50)
    siteaddr = models.CharField(max_length=50)
    hosted = models.CharField(max_length=50)
    hours = models.CharField(max_length=50)
    notes = models.TextField()
    website = models.CharField(max_length=50)
    bin = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name
