from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    """
    Admin configuration for the Booking model.

    This class defines the administration interface for the Booking model,
    allowing administrators to view, search, and edit booking records.
    It uses SummernoteModelAdmin to provide a rich text editor for the 'notes' field.
    """

    list_display = ['name', 'email', 'phone_number', 'service_type', 'date_preference', 'time_preference']
    search_fields = ['name', 'email', 'phone_number', 'service_type']
    summernote_fields = ['notes']