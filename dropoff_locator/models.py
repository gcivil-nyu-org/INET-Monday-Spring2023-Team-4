from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    BOROUGHS = [
        ("Manhattan", "Manhattan"),
        ("Brooklyn", "Brooklyn"),
        ("Queens", "Queens"),
        ("Bronx", "Bronx"),
        ("Staten Island", "Staten Island"),
    ]
    OPEN_MONTHS = [
        ("Year Round", "Year Round"),
        ("Seasonal", "Seasonal"),
    ] 
    SITE_TYPES = [
        ("Smart Bin", "NYC Smart Bin"),
        ("Community", "NYC Community Site"),
        ("User", "User Listing"),
    ]
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    borough = models.CharField(max_length=20, choices=BOROUGHS)
    type = models.CharField(max_length=30, choices=SITE_TYPES)
    schedule = models.CharField(max_length=15, choices=OPEN_MONTHS)
    season_start = models.CharField(max_length=25)
    season_end = models.CharField(max_length=25)
    day_hours = models.CharField(max_length=225)
    lat = models.FloatField()
    lon = models.FloatField()    
    notes = models.TextField()

    def __str__(self):
        return self.name

class NYCHost(models.Model):
    name = models.CharField(max_length=225, primary_key=True)
    url = models.CharField(max_length=225)
    sites = models.ManyToManyField(Site, through='NYCSiteHost', related_name="hosts")

    def __str__(self):
        return self.name

class NYCSiteHost(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    host = models.ForeignKey(NYCHost, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.site.__str__(), self.host.__str__())





