from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta


class Booking(models.Model):
    """
    Model representing a booking for a service.
    """
    SERVICE_CHOICES = [
        ('haircut', 'Haircut'),
        ('coloring', 'Coloring'),
        ('styling', 'Styling'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    date_preference = models.DateField()
    time_preference = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of a booking.
        """
        return f'{self.name} - {self.service_type} - {self.date_preference} {self.time_preference}'

    def clean_date_preference(self):
        """
        Custom validation for the date preference field.
        """
        date_preference = self.cleaned_data.get('date_preference')
        if date_preference:
            # Determine today's date
            today = date.today()
            # Add one day to today's date
            next_day = today + timedelta(days=1)
            
            # Check if the selected date is on or after the next day
            if next_day < date_preference:
                raise ValidationError(_('Booking can only be made for the next business day.'))
            
            # Check if the selected date is Sunday, Monday, or Tuesday
            if date_preferece.weekday() in [6, 0, 1]:
                raise ValidationError(_('Invalid date - cannot book on Sundays, Mondays, or Tuesdays'))
        return date_preference