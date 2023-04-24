from django.db import models


class Site(models.Model):
    BOROUGHS = [
        ("Manhattan", "Manhattan"),
        ("Brooklyn", "Brooklyn"),
        ("Queens", "Queens"),
        ("Bronx", "Bronx"),
        ("Staten Island", "Staten Island"),
    ]
    SCHEDULE_TYPES = [
        ("Year Round", "Year Round"),
        ("Seasonal", "Seasonal"),
    ]
    SITE_TYPES = [
        ("NYC Smart Bin", "NYC Smart Bin"),
        ("NYC Community Site", "NYC Community Site"),
        ("User Listing", "User Listing"),
    ]
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    borough = models.CharField(max_length=15, choices=BOROUGHS)
    type = models.CharField(max_length=30, choices=SITE_TYPES)
    season = models.CharField(max_length=15, choices=SCHEDULE_TYPES)
    is_always_open = models.BooleanField()
    lat = models.FloatField()
    lon = models.FloatField()
    notes = models.TextField()

    def __str__(self):
        return self.name
