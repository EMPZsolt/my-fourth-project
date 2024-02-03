from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    date_preference = forms.DateField(
        label = 'Date',
        widget=forms.DateInput(attrs={'type': 'date'}))
    time_preference = forms.TimeField(
        label = 'Time',
        widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'service_type', 'notes', 'date_preference', 'time_preference']