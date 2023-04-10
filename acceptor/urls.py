from django.urls import path
from .views import acceptor

urlpatterns = [
    path("", acceptor, name="acceptor_view"),
]
