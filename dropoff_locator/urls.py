from django.urls import path, include
from . import views

app_name = "dropoff_locator"

urlpatterns = [
    path("", views.locations, name="locator_view"),
]
