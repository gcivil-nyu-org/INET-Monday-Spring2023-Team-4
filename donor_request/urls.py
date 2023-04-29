from django.urls import path
from . import views

app_name = "donor_request"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("<int:pk>/", views.request_thread, name="request_thread"),
    path("new-request/<int:pk>/", views.create_request, name="create_request"),
]
