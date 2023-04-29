from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dropoff_locator.models import Site
from users.models import Profile
from .models import Request, Message
from .forms import MessageForm
from .filters import RequestFilter


# donor required
@login_required
def create_request(request, pk):
    user = request.user.profile
    site = get_object_or_404(Site, pk=pk)
    host = site.hosts.first()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            new_request = Request(donor=user, host=host, site=site)
            new_request.save()
            initial_message = Message(request=new_request, sender=user, text=text)
            initial_message.save()
            messages.success(request, "Request Sent")
            return redirect(to="dropoff_locator:site_details", pk=pk)

    form = MessageForm()
    context = {
        "form": form,
        "user": user,
        "site": site,
        "host": host,
    }
    return render(request, "donor_request/request.html", context)


@login_required
def send_response(request, pk):
    curr_request = Request.objects.get(pk=pk)
    user = request.user.profile

    # pk is response_id
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            new_message = Message(request=curr_request, sender=user, text=text)
            new_message.save()
            messages.success(request, "Request Sent")
            return redirect(to="request_thread", pk=pk)

    form = MessageForm()

    context = {
        "form": MessageForm(),
        # "request": curr_request,
        # "sender": user,
        # "receiver": curr_request.host if user is curr_request.donor else curr_request.donor,
    }
    return render(request, "donor_request/response.html", context)


def view_thread(request, pk):
    pass


@login_required
def inbox(request):
    user = request.user.profile

    if request.session["profile"] == "donor":
        user_requests = RequestFilter(
            request.GET, queryset=Request.objects.filter(donor=user).order_by("-updated")
        )
        context = {"form": user_requests.form, "requests": user_requests.qs}
        return render(request, "donor_request/inbox.html", context)
    elif request.session["profile"] == "host":
        user_requests = RequestFilter(
            request.GET, queryset=Request.objects.filter(host=user).order_by("-updated")
        )
        context = {"form": user_requests.form, "requests": user_requests.qs}
        return render(request, "donor_request/inbox.html", context)

def request_thread(request, pk):
    user_request = get_object_or_404(Request, pk=pk)
    thread = Message.objects.filter(request=user_request).order_by("-date")
    context = {"request": user_request, "messages": thread}
    return render(request, "donor_request/view_request.html", context)
