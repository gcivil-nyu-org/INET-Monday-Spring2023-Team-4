from django.urls import path, include
from . import views

app_name = "acceptor"

urlpatterns = [
    path("main/", views.dashboard, name="acceptor_view"),
    path("new-site/", views.create_listing, name="new_site"),
    path("<int:pk>/edit/", views.update_listing, name="edit_site"),
    path("<int:pk>/delete/", views.delete_listing, name="delete_site"),
    #path("map/", include("dropoff_locator.urls", namespace="dropoff_locator")),
]



