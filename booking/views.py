from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful! Thank you.')
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/book_service.html', {'form': form})

@login_required
def booking_success(request):
    return render(request, 'booking/booking_success.html')

@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'booking/booking_detail.html', {'booking': booking})