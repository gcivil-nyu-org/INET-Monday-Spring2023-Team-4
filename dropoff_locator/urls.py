from django.urls import path
from .views import locations, site_details
from donor_request.views import create_request

app_name = "dropoff_locator"

urlpatterns = [
    path("", locations, name="locator_view"),
    path("<int:pk>/", site_details, name="site_details"),
    path("<int:pk>/new-request", create_request, name="create_request"),
]
