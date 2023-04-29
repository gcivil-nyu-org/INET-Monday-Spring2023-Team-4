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

    def get_season(self):
        if self.type != "User Listing":
            if self.season == "Seasonal":
                season = SiteSeason.objects.filter(site=self).get()
                return season

    def get_schedule(self):
        if self.type != "User Listing":
            if self.is_always_open is False:
                schedule = SiteSchedule.objects.filter(site=self).get()
                return schedule


class SiteSeason(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, primary_key=True)
    start = models.CharField(max_length=15)
    end = models.CharField(max_length=15)


class SiteSchedule(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, primary_key=True)
    mon = models.CharField(max_length=55, null=True)
    tues = models.CharField(max_length=55, null=True)
    wed = models.CharField(max_length=55, null=True)
    thurs = models.CharField(max_length=55, null=True)
    fri = models.CharField(max_length=55, null=True)
    sat = models.CharField(max_length=55, null=True)
    sun = models.CharField(max_length=55, null=True)
