from django.urls import path
from . import views

app_name = "dropoff_locator"

urlpatterns = [
    path("", views.locations, name="locator_view"),
    path("<int:pk>/", views.site_details, name="site_details"),
]
