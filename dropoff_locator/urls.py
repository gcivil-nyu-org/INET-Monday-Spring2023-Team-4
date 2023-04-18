from django.urls import path, include
from . import views

app_name = "dropoff_locator"

urlpatterns = [
    path('', views.index, name="map"),
    path('<int:pk>/', views.site, name="site-details")
]