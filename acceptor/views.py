from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import NewSiteForm
from users.models import Profile, SiteHost
from dropoff_locator.models import Site, Item, SiteAccepted


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

        # create new site
        if form.is_valid():
            new_site = form.save()
            new_site.lat = 40.69438
            new_site.lon = -73.98648
            new_site.save()

        # add site to user's profile
        self = Profile.objects.get(user=request.user)
        self.sites.add(new_site)

        return redirect(to="acceptor:acceptor_view")

    # lat/lon -> get from googlemaps api using address and borough provided, use prefilled values for now
    initial_data = {
        "type": "User Listing",
        "is_always_open": False,
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
            SiteAccepted.objects.filter(site=site).delete()
            SiteHost.objects.filter(site=site).delete()
            site.delete()
            messages.success(request, "Listing Deleted")
        return redirect("acceptor:acceptor_view")

    return render(request, "acceptor/delete_site.html", {"site": site})
