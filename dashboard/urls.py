from django.urls import path, include
from . import views

app_name = "donor"

urlpatterns = [
    path("", views.main, name="dashboard"),
    path("messages/", include("donor_request.urls", namespace="donor_request")),
    # maybe some activity tracker
]
