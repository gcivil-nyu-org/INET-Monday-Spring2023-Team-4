from django.urls import path
from .views import locations, site_details
from donor_request.views import create_request as donor_new_request

app_name = "dropoff_locator"

urlpatterns = [
    path("", locations, name="locator_view"),
    path("<int:pk>/", site_details, name="site_details"),
    path("<int:pk>/new-request/", donor_new_request, name="new_request"),
]


