
// Select all edit and delete buttons
const editButtons = document.querySelectorAll(".btn-warning");
const deleteButtons = document.querySelectorAll(".btn-danger");

// Get the delete confirmation modal
const deleteConfirm = document.getElementById("deleteConfirm");

// Edit functionality
editButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Get booking details from data attributes
        const bookingId = button.getAttribute("data-booking_id");
        const bookingName = document.getElementById(`bookingName${bookingId}`).innerText;
        const bookingEmail = document.getElementById(`bookingEmail${bookingId}`).innerText;
        const bookingPhoneNumber = document.getElementById(`bookingPhoneNumber${bookingId}`).innerText;
        const bookingServiceType = document.getElementById(`bookingServiceType${bookingId}`).innerText;
        const bookingNotes = document.getElementById(`bookingNotes${bookingId}`).innerText;
        const bookingDatePreference = document.getElementById(`bookingDatePreference${bookingId}`).innerText;
        const bookingTimePreference = document.getElementById(`bookingTimePreference${bookingId}`).innerText;

        // Populate form fields with booking details
        document.getElementById("id_name").value = bookingName;
        document.getElementById("id_email").value = bookingEmail;
        document.getElementById("id_phone_number").value = bookingPhoneNumber;
        document.getElementById("id_service_type").value = bookingServiceType;
        document.getElementById("id_notes").value = bookingNotes;
        document.getElementById("id_date_preference").value = bookingDatePreference;
        document.getElementById("id_time_preference").value = bookingTimePreference;

        // Change submit button text and form action
        document.getElementById("submitButton").innerText = "Update";
        document.getElementById("bookingForm").setAttribute("action", `modify_booking/${bookingId}`);
    });
});


// Delete functionality
deleteButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Get booking ID from data attribute and set delete confirmation link
        const bookingId = button.getAttribute("data-booking_id");
        deleteConfirm.href = `delete_booking/${bookingId}`;
        
        // Show delete confirmation modal
        deleteModal.show();
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Define an array of disabled days (0: Sunday, 1: Monday, 2: Tuesday)
    const disabledDays = [0, 1, 2]; // Sundays, Mondays, Tuesdays are disabled

    // Get the date input field
    const dateInput = document.querySelector('#id_date_preference');

    // Check if the date input field exists
    if (dateInput) {
        // Add an event listener for input changes on the date input field
        dateInput.addEventListener('input', function () {
            // Parse the selected date from the input field
            const selectedDate = new Date(dateInput.value);

            // Check if the selected date is valid
            if (isNaN(selectedDate.getTime())) {
                alert('Invalid date format. Please select a valid date.');
                dateInput.value = ''; // Clear the input value
                return; // Exit the function, do not continue
            }

            // Get the day of the week (0 for Sunday, 1 for Monday, ..., 6 for Saturday)
            const selectedDay = selectedDate.getDay();

            // Check if the selected day is in the disabledDays array
            if (disabledDays.includes(selectedDay)) {
                alert('Invalid date - we are closed on Sundays, Mondays, or Tuesdays.');
                dateInput.value = ''; // Reset the input value
            }
        })
    }
})