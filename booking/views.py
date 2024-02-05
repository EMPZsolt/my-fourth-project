from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@login_required
def book_service(request):

    """
    View for booking a service.
    If request method is POST, processes the form submission,
    saves the booking, and redirects to booking page with success message.
    If request method is GET, renders the booking form.
    Retrieves user's bookings and renders them on the page.
    """

    if request.method == 'POST':
        # If the request method is POST, process the form submission
        form = BookingForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the booking
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Thank you! Successful booking request. I will send you feedback the next business day to confirm.')
            return redirect('booking')
    else:
        # If the request method is GET, render the booking form
        form = BookingForm()
    
    # Retrieve user's bookings and render them on the page
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/book_service.html', {'form': form, 'bookings': bookings})


@login_required
def booking_detail(request, pk):

    """
    View for rendering the details of a booking.
    Retrieves the booking object with the specified primary key
    and renders the booking detail form.
    """

    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    form = BookingForm(instance=booking)
    return render(request, 'booking/booking_detail.html', {'form': form, 'booking': booking})


@login_required
def modify_booking(request, pk):

    """
    View for modifying a booking.
    Retrieves the booking object with the specified primary key,
    processes the form submission, saves the modified booking,
    and redirects to the booking page with success message.
    """

    # Retrieve the booking object with the specified primary key
    booking = get_object_or_404(Booking, pk=pk)
    
    # Check if the logged-in user is the owner of the booking
    if booking.user != request.user:
        # If not, raise a PermissionDenied exception
        raise PermissionDenied
    
    if request.method == 'POST':
        # If the request method is POST, process the form submission
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            # If the form is valid, save the modified booking
            form.save()
            messages.success(request, 'Thank you! Successful booking request update. I will send you feedback the next business day to confirm.')
            return redirect('booking')
    else:
        # If the request method is GET, render the booking detail form
        form = BookingForm(instance=booking)
    
    # Render the booking detail form
    return render(request, 'booking/booking_detail.html', {'form': form, 'booking': booking})


@login_required
def delete_booking(request, pk):

    """
    View for deleting a booking.
    Retrieves the booking object with the specified primary key,
    deletes the booking, and redirects to the booking page with success message.
    """
    
    # Retrieve the booking object with the specified primary key
    booking = get_object_or_404(Booking, pk=pk)
    
    # Check if the logged-in user is the owner of the booking
    if booking.user != request.user:
        # If not, raise a PermissionDenied exception
        raise PermissionDenied
    
    if request.method == 'POST':
        # If the request method is POST, delete the booking
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('booking')
    else:
        # If the request method is not POST, redirect to the booking page
        return HttpResponseRedirect(reverse('booking'))