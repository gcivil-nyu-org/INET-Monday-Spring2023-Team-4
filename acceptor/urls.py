from django.urls import path
from .views import acceptor

urlpatterns = [
    path("<int:pk>/acceptor/", acceptor, name="acceptor_view"),
]
