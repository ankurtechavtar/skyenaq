jQuery('#contact-form').on('submit', function(e) {
    e.preventDefault(); // Prevent page refresh

    jQuery.ajax({
        url: '/submit-form/',  // Django view URL
        data: jQuery(this).serialize(),
        type: 'POST',
        headers: { "X-CSRFToken": getCookie("csrftoken") }, // CSRF token for security
        success: function(response) {
            if (response.status === "success") {
                swal({
                    title: "Thank You!",
                    text: response.message,
                    icon: "success",
                    timer: 3000
                }).then(function() {
                    jQuery('#contact-form')[0].reset();
                });
            } else {
                swal({
                    title: "Oops...",
                    text: response.message,
                    icon: "error",
                    timer: 3000
                });
            }
        },
        error: function() {
            swal({
                title: "Error",
                text: "Something went wrong!",
                icon: "error",
                timer: 3000
            });
        }
    });
});

// Function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
