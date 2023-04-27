from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import NewSiteForm
from users.models import Profile, SiteHost
from dropoff_locator.models import Site


@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    sites = profile.sites.all()
    context = {"user": request.user, "sites": sites}
    return render(request, "acceptor/acceptor.html", context)


@login_required
def create_listing(request):
    if request.method == "POST":
        form = NewSiteForm(request.POST)
        # add site to site table
        new_site = form.save()

        # add site and user to sitehost table
        self = Profile.objects.get(user=request.user)
        SiteHost(site=new_site, host=self).save()

        messages.success(request, "Listing Added Successfully")
        return redirect(to="acceptor:acceptor_view")

    # lat/lon -> get from googlemaps api using address and borough provided, use prefilled values for now
    initial_data = {
        "type": "User Listing",
        "is_always_open": False,
        "lat": 40.69438,
        "lon": -73.98648,
    }
    context = {"form": NewSiteForm(initial=initial_data)}
    return render(request, "acceptor/new_site.html", context)


@login_required
def update_listing(request, pk):
    site = get_object_or_404(Site, pk=pk)
    form = NewSiteForm(request.POST or None, instance=site)

    if form.is_valid():
        form.save()
        messages.success(request, "Listing Updated")
        return redirect("acceptor:acceptor_view")

    return render(request, "acceptor/edit_site.html", {"form": form})


@login_required
def delete_listing(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        if "confirm" in request.POST:
            site.delete()
            messages.success(request, "Listing Deleted")
        return redirect("acceptor:acceptor_view")

    return render(request, "acceptor/delete_site.html", {"site": site})
