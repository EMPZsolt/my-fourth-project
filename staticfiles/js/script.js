
// Edit and delete buttons
const editButtons = document.querySelectorAll(".btn-warning");
const deleteButtons = document.querySelectorAll(".btn-danger");

// Delete modal
const deleteConfirm = document.getElementById("deleteConfirm");

// Edit functionality
editButtons.forEach(button => {
    button.addEventListener("click", () => {
        const bookingId = button.getAttribute("data-booking_id");
        const bookingName = document.getElementById(`bookingName${bookingId}`).innerText;
        const bookingEmail = document.getElementById(`bookingEmail${bookingId}`).innerText;
        const bookingPhoneNumber = document.getElementById(`bookingPhoneNumber${bookingId}`).innerText;
        const bookingServiceType = document.getElementById(`bookingServiceType${bookingId}`).innerText;
        const bookingNotes = document.getElementById(`bookingNotes${bookingId}`).innerText;
        const bookingDatePreference = document.getElementById(`bookingDatePreference${bookingId}`).innerText;
        const bookingTimePreference = document.getElementById(`bookingTimePreference${bookingId}`).innerText;

        document.getElementById("id_name").value = bookingName;
        document.getElementById("id_email").value = bookingEmail;
        document.getElementById("id_phone_number").value = bookingPhoneNumber;
        document.getElementById("id_service_type").value = bookingServiceType;
        document.getElementById("id_notes").value = bookingNotes;
        document.getElementById("id_date_preference").value = bookingDatePreference;
        document.getElementById("id_time_preference").value = bookingTimePreference;

        document.getElementById("submitButton").innerText = "Update";
        document.getElementById("bookingForm").setAttribute("action", `modify_booking/${bookingId}`);
    });
});

// Delete functionality
deleteButtons.forEach(button => {
    button.addEventListener("click", () => {
        const bookingId = button.getAttribute("data-booking_id");
        deleteConfirm.href = `delete_booking/${bookingId}`;
        deleteModal.show();
    });
});