from django.shortcuts import render, redirect, get_object_or_404
from .models import Request, Message
from dropoff_locator.models import Site
from .forms import MessageForm
from django.contrib.auth.decorators import login_required


@login_required
def has_open_request(request, site_id):
    user = request.user
    site = get_object_or_404(Site, pk=site_id)
    requests = Request.objects.filter(status="Open").filter(donor=user)
    return requests.filter(site=site).exists()


def create_request(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    host = site.hosts.first()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            new_request = Request(donor=request.user, site=site_id, status="Open")
            request.save()
            message = Message(request=new_request, sender=request.user, text=text)
            message.save()
            print("Success!")
            return redirect(to="site_details", pk=site_id)

    form = MessageForm()
    context = {"form": form, "donor": request.user, "site": site, "host": host}
    return render(request, "request.html", context)


@login_required
def inbox(request):
    #     user = request.user
    #     sent = Message.objects.filter(sender=user)
    #     received = Message.objects.filter(receiver=user)
    #     context = {"user": user, "sent": sent, "received": received}
    # return render(request, "inbox.html", context)
    return render("inbox.html")