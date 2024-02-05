from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.my_salon, name="home"),
    path("booking/", include("booking.urls"), name="booking"),
]