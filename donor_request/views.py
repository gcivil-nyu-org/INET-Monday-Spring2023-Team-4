from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dropoff_locator.models import Site
from users.models import Profile
from .models import Request, Message
from .forms import MessageForm
from .filters import RequestFilter


#donor required
@login_required
def create_request(request, pk):
    user = request.user.profile
    site = get_object_or_404(Site, pk=pk)
    host = site.hosts.first()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            new_request = Request(donor=user, site=site).save()
            initial_message = Message(request=new_request, sender=user, text=text)
            initial_message.save()
            messages.success(request, "Request Sent")
            return redirect(to="site_details", pk=pk)

    form = MessageForm()
    context = {"form": form, "user": user, "site": site, "host": host,}
    return render(request, "donor_request/request.html", context)


@login_required
def send_response(request, pk):
    curr_request = Request.objects.get(pk=pk)
    user = request.user.profile
    
    #pk is response_id
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
        #"request": curr_request, 
        #"sender": user, 
        #"receiver": curr_request.host if user is curr_request.donor else curr_request.donor,
    }
    return render(request, "donor_request/response.html", context)


def view_thread(request, pk):
    pass

@login_required
def inbox(request):
    if request.method == 'POST':
        user = request.user.profile    
        filter = RequestFilter(request.GET, queryset=Request.objects.filter(donor=user))
        context = {"form": filter.form, "requests": filter.qs}
        return render(request, "donor_request/inbox.html", context)
    


    #     user = request.user
    #     sent = Message.objects.filter(sender=user)
    #     received = Message.objects.filter(receiver=user)
    #     context = {"user": user, "sent": sent, "received": received}
    # return render(request, "inbox.html", context)
    return render("donor_request:inbox.html")


def request_thread(request):
    pass

