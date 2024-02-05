from datetime import date, timedelta
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for booking a service.
    """
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'service_type', 'notes', 'date_preference', 'time_preference']
        widgets = {
            'date_preference': forms.DateInput(attrs={'type': 'date', 'min': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')}),
        }

    def clean_date_preference(self):
        """
        Validates the date preference field.
        """
        date_preference = self.cleaned_data.get('date_preference')
        if date_preference < date.today():
            raise ValidationError(_('Invalid date - cannot be in the past'))
        return date_preference