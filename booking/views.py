from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data and create a new Booking object
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the current user to the booking
            booking.save()

            # Display a success message
            messages.success(request, 'Booking successful! Thank you.')
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, 'booking/book_service.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/booking_success.html')