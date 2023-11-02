$(document).ready(function () {
    $('form').submit(function (e) {
        e.preventDefault();
        var form = $(this);

        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            success: function (data) {
                if (data.error) {
                    swal("Error", data.error, "error");
                } else {
                    swal("Success", data.message, "success");
                    form[0].reset();  // Clear the form after successful submission
                }
            },
            error: function () {
                swal("Error", "An error occurred while processing your request.", "error");
            }
        });
    });
});