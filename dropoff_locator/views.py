from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from filters import SiteFilter

# from .services import get_locations
from .models import Site, NYCHost, NYCSiteHost

def index(request):
    site_filter = SiteFilter(request.GET, queryset=Site.objects.all())
    context = {
        "form": site_filter.form,
        "locations": site_filter.qs
        }
    return render(request, "locations.html", context)

def site(request, pk):
    site = get_object_or_404(Site, pk=pk)
    hosts = site.hosts.all()
    context = {"site": site,
               "hosts": hosts
               }
    return render(request, "sitedetails.html", context)