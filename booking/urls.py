from django.urls import path
from . import views


urlpatterns = [
    path('book-service/', views.book_service, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('booking/<int:pk>/detail/', views.booking_detail, name='booking_detail'),
    path('booking/<int:pk>/modify/', views.modify_booking, name='modify_booking'),
    path('booking/<int:pk>/delete/', views.delete_booking, name='delete_booking'),
]