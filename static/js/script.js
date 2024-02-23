let isPageRefreshed = false;

document.addEventListener('DOMContentLoaded', function() {
    addEventListenersToButtons();
    addEventListenersToDateInput();
    addEventListenersToCancelButtons(); // Added event listeners to cancel buttons
});

function addEventListenersToButtons() {
    // Add event listeners for edit buttons
    document.querySelectorAll('.btn-edit').forEach(button => {
        button.addEventListener('click', function() {
            var reviewId = this.getAttribute('data-review-id');
            toggleEdit(reviewId);
        });
    });

    // Add event listeners for save buttons
    document.querySelectorAll('.btn-save').forEach(button => {
        button.addEventListener('click', function() {
            var reviewId = this.getAttribute('data-review-id');
            saveEdit(reviewId);
        });
    });

    // Add event listeners for delete buttons
    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', function() {
            var reviewId = this.getAttribute('data-review-id');
            deleteReview(reviewId);
        });
    });

    // Add event listeners for cancel review buttons
    document.querySelectorAll('.btn-cancel-review').forEach(button => {
        button.addEventListener('click', function() {
            var reviewId = this.getAttribute('data-review-id');
            cancelEdit(reviewId);
        });
    });
}

function toggleEdit(reviewId) {
    var editForm = document.getElementById('edit-form-' + reviewId);
    editForm.style.display = (editForm.style.display === 'none') ? '' : 'none';

    var editButton = document.querySelector('#review-' + reviewId + ' .btn-edit');
    var deleteButton = document.querySelector('#review-' + reviewId + ' .btn-delete');
    editButton.style.display = (editForm.style.display === 'none') ? '' : 'none';
    deleteButton.style.display = (editForm.style.display === 'none') ? '' : 'none';
}

function cancelEdit(reviewId) {
    toggleEdit(reviewId);
}

function saveEdit(reviewId) {
    var textarea = document.getElementById('edit-content-' + reviewId);
    var content = textarea.value;
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(`/user_profile/edit_review/${reviewId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ content: content })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('review-content-text-' + reviewId).innerText = content;
            toggleEdit(reviewId);
            
            // Optionally, you can update the content without reloading the page
        } else {
            alert('Error updating review.');
        }
    });
}

function deleteReview(reviewId) {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
    }).then((result) => {
        if (result.isConfirmed) {
            // If user confirms deletion, proceed with the deletion request
            var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(`/user_profile/delete_review/${reviewId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                        // Refresh the page after displaying the success message
                        location.reload();
                } else {
                    // Handle deletion failure, if needed
                    Swal.fire({
                        title: "Error!",
                        text: "Failed to delete review.",
                        icon: "error"
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle deletion failure, if needed
                Swal.fire({
                    title: "Error!",
                    text: "Failed to delete review.",
                    icon: "error"
                });
            });
        }
    });
}




function addEventListenersToDateInput() {
    const dateInput = document.getElementById('id_date');

    if (dateInput) {
        // Get the current date in 'yyyy-mm-dd' format
        const currentDate = new Date().toISOString().slice(0, 10);

        // Set the value of the date input field to the current date
        dateInput.value = currentDate;

        // Fetch available time slots for the current date
        fetchAvailableTimeSlots(currentDate);

        // Add change event listener to date input field
        dateInput.addEventListener('change', function() {
            fetchAvailableTimeSlots(this.value);
        });
    } else {
        console.error('Date input field not found');
    }
}

function fetchAvailableTimeSlots(date) {
    fetch(`ajax/get_available_time_slots/?date=${date}`)
        .then(response => response.json())
        .then(data => {
            data.time_slots.forEach(slot => {
                const input = document.querySelector(`input[value="${slot.time}"]`);
                if (input) {
                    input.disabled = slot.booked;
                }
            });
        })
        .catch(error => console.error('Error fetching available time slots:', error));
}

function addEventListenersToCancelButtons() {
    // Add event listeners for cancel booking buttons
    document.querySelectorAll('.btn-cancel-booking').forEach(button => {
        button.addEventListener('click', function() {
            var bookingId = this.getAttribute('data-booking-id');
            cancelBooking(bookingId);
        });
    });
}

function cancelBooking(bookingId) {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, cancel it!"
    }).then((result) => {
        if (result.isConfirmed) {
            // If user confirms cancellation, proceed with the cancellation request
            var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(`/user_profile/cancel_booking/${bookingId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('booking-' + bookingId).remove();
                    if (!isPageRefreshed) {
                        isPageRefreshed = true;
                        // Optionally, display a success message here
                        Swal.fire({
                            title: "Canceled!",
                            text: "Your booking has been canceled.",
                            icon: "success"
                        }).then(() => {
                            // Refresh the page
                            location.reload();
                        });
                    }
                } else {
                    // Handle cancellation failure, if needed
                    Swal.fire({
                        title: "Error!",
                        text: "Failed to cancel booking.",
                        icon: "error"
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle cancellation failure, if needed
                Swal.fire({
                    title: "Error!",
                    text: "Failed to cancel booking.",
                    icon: "error"
                });
            });
        }
    });
}