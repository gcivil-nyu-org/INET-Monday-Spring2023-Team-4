from django.urls import path
from . import views

app_name = "donor_request"

urlpatterns = [
    path("", views.inbox, name="inbox"),
]
