from django.urls import path
from . import views
from donor_request.views import create_request

app_name = "dropoff_locator"

urlpatterns = [
    path("", views.locations, name="locator_view"),
    path("<int:pk>/", views.site_details, name="site_details"),
    path("<int:pk>/new-request", create_request, name="create_request"),
]
