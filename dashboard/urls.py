from django.urls import path, include
from . import views
from dropoff_locator.views import locations

app_name = "donor"

urlpatterns = [
    path("", locations, name="dashboard"),
    path("messages/", include("donor_request.urls", namespace="donor_request")),
    # maybe some activity tracker
]
