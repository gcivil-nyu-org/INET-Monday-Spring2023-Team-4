from django.urls import path
from . import views

app_name = "donor_request"

urlpatterns = [
    path("<int:pk>/request", views.create_request, name="create_request"),
]