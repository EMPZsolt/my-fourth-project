from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_salon, name='home'),
]