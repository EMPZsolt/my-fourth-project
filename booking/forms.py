from datetime import date
from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class BookingForm(forms.ModelForm):
    date_preference = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )


    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'service_type', 'notes', 'date_preference', 'time_preference']


    def clean_date_preference(self):
        date_preference = self.cleaned_data.get('date_preference')
        if date_preference and date_preference < date.today():
            raise ValidationError(_('Invalid date - cannot be in the past'))
        return date_preference