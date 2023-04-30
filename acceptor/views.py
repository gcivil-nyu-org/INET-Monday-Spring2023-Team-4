from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import http
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from users.models import Profile, SiteHost
from dropoff_locator.models import Site, SiteAccepted


@login_required
def dashboard(request):
    sites = request.user.profile.sites.all()

    if request.method == "POST":
        ntaname = request.POST["ntaname"]
        siteaddr = request.POST["siteaddr"]
        # fromtime = request.POST["fromtime"]
        # totime = request.POST["totime"]
        # website = request.POST["website"]
        borough = request.POST["borough"]
        lat = request.POST["lat"]
        lon = request.POST["lon"]
        notes = request.POST["notes"]
        # accepted_items = request.POST["accepted_items"]

        data = Site(
            name=ntaname,
            address=siteaddr,
            # hours="From" + fromtime + "to" + totime,
            # website=website,
            borough=borough,
            lat=lat,
            lon=lon,
            notes=notes,
            # accepted_items=accepted_items,
            # hosted=request.user.username,
        )

        data.save()
        self = request.user.profile
        self.sites.add(data)

        messages.success(request, "Bin Added Successfully.")
        return redirect(to="acceptor:acceptor_view")

    context = {"user": request.user, "sites": sites}
    return render(request, "acceptor/acceptor.html", context)

    # messages.success(request, "Bin Added Successfully.")
    #     return redirect(to="acceptor_view")

    # if request.method == "POST":
    #     form = NewSiteForm(request.POST)

    #     # create new site
    #     if form.is_valid():
    #         new_site = form.save()
    #         new_site.lat = 40.69438
    #         new_site.lon = -73.98648
    #         new_site.save()

    #         # add site to user's profile
    #         self = request.user.profile
    #         self.sites.add(new_site)

    #     return redirect(to="acceptor:acceptor_view")

    # lat/lon -> get from googlemaps api using address and borough provided, use prefilled values for now
    # context = {"form": NewSiteForm()}
    # return render(request, "acceptor/acceptor.html", context)


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
