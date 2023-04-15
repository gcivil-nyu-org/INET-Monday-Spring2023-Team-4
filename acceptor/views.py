from django.shortcuts import render
from dashboard.models import dashboard
from django.contrib.auth.decorators import login_required

@login_required
def acceptor(request):
    bins = dashboard.objects.all()
    context = {"bins": bins}
    return render(request, "acceptor/acceptor.html", context)

