from django.shortcuts import render, get_object_or_404
from .filters import SiteFilter
from .models import Site


def locations(request):
    site_filter = SiteFilter(request.GET, queryset=Site.objects.all())
    context = {"form": site_filter.form, "locations": site_filter.qs}
    return render(request, "locations.html", context)


def site_details(request, pk):
    site = get_object_or_404(Site, pk=pk)
    hosts = site.hosts.all()
    season = site.get_season()
    schedule = site.get_schedule()
    context = {
        "location": site,
        "hosts": hosts,
        "season": season,
        "schedule": schedule,
    }
    return render(request, "site_details.html", context)
