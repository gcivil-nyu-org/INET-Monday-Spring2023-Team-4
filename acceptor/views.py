from django.shortcuts import render, redirect
from dashboard.models import dashboard
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


@login_required
def acceptor(request):
    if request.method == "POST":
        ntaname = request.POST["ntaname"]
        siteaddr = request.POST["siteaddr"]
        fromtime = request.POST["fromtime"]
        totime = request.POST["totime"]
        website = request.POST["website"]
        borough = request.POST["borough"]
        lat = request.POST["lat"]
        lon = request.POST["lon"]
        notes = request.POST["notes"]

        data = dashboard(
            ntaname=ntaname,
            siteaddr=siteaddr,
            hours="From" + fromtime + "to" + totime,
            website=website,
            borough=borough,
            lat=lat,
            lon=lon,
            notes=notes,
            hosted=request.user.username,
        )

        data.save()
        messages.success(request, "Bin Added Successfully.")
        return redirect(to="acceptor_view")

    bins = dashboard.objects.all()
    context = {"bins": bins}
    return render(request, "acceptor/acceptor.html", context)
