from django.urls import path, include
from . import views

app_name = "dropoff_locator"

urlpatterns = [
    path('', views.locations, name="map"),
    path('<int:pk>/', views.site_details, name="site-details")
]