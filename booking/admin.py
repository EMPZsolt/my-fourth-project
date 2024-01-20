from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'service_type', 'date_preference', 'time_preference']
    search_fields = ['name', 'email', 'phone_number', 'service_type']
    summernote_fields = ['notes']

# Register your models here.

