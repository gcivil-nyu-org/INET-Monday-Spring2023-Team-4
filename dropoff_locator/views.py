from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .filters import SiteFilter
from .models import Site

@login_required
def locations(request):
    site_filter = SiteFilter(request.GET, queryset=Site.objects.all())
    context = {"form": site_filter.form, "locations": site_filter.qs}
    return render(request, "locations.html", context)

@login_required
def site_details(request, pk):
    site = get_object_or_404(Site, pk=pk)
    accepted_items = site.accepted_items.all()
    hosts = site.hosts.all()
    season = site.get_season()
    schedule = site.get_schedule()
    user = request.session["profile"]
    context = {
        "location": site,
        "hosts": hosts,
        "season": season,
        "schedule": schedule,
        "items": accepted_items,
        "user": user,
    }
    return render(request, "site_details.html", context)
