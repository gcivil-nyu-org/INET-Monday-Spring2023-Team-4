from django.shortcuts import render


def acceptor(request):
    return render(request, "acceptor/acceptor.html")
