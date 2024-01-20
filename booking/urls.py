from django.urls import path
from . import views


urlpatterns = [
    path('book-service/', views.book_service, name='book_service'),
    path('success/', views.booking_success, name='booking_success'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
]