// JavaScript function to display booking success message

document.addEventListener("DOMContentLoaded", function() {
    const modifyForm = document.getElementById("modifyForm");
    const modifyButton = document.getElementById("modifyButton");
    const deleteForm = document.getElementById("deleteForm");
    const deleteButton = document.getElementById("deleteButton");
  
    // Modify Booking Functionality
    modifyForm.addEventListener("submit", function(event) {
      event.preventDefault();
    });
  
    // Delete Booking Functionality
    deleteForm.addEventListener("submit", function(event) {
      event.preventDefault();
      if (confirm("Are you sure you want to delete this booking?")) {
      }
    });
  });