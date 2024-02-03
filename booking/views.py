from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


"""
View for booking a service.
If request method is POST, processes the form submission,
saves the booking, and redirects to booking page with success message.
If request method is GET, renders the booking form.
Retrieves user's bookings and renders them on the page.
"""
@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Thank you! Successful booking request. I will send you feedback the next business day to confirm.')
            return redirect('booking')
    else:
        form = BookingForm()
    
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/book_service.html', {'form': form, 'bookings': bookings})


"""
View for rendering the details of a booking.
Retrieves the booking object with the specified primary key
and renders the booking detail form.
"""
@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    form = BookingForm(instance=booking)
    return render(request, 'booking/booking_detail.html', {'form': form, 'booking': booking})


"""
View for modifying a booking.
Retrieves the booking object with the specified primary key,
processes the form submission, saves the modified booking,
and redirects to the booking page with success message.
"""
@login_required
@permission_required('auth.change_booking', raise_exception=True)
def modify_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you! Booking updated successfully! I will send you feedback the next business day to confirm.')
            return redirect('booking')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_detail.html', {'form': form, 'booking': booking})


"""
View for deleting a booking.
Retrieves the booking object with the specified primary key,
deletes the booking, and redirects to the booking page with success message.
"""
@login_required
@permission_required('auth.delete_booking', raise_exception=True)
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted successfully.')
        return redirect('booking')
    return HttpResponseRedirect(reverse('booking'))