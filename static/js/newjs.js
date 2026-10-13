$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#container2').hide();
    $('#sol').hide();
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        $('#sol').text('');
        $('#sol').hide();
        readURL(this);
    });
    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();
        $('#container2').fadeIn(500);
        $('#container2').show();
        $('html, body').animate({
            scrollTop: $('#container2').offset().top
        }, 1000);


        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#container2').show();
                $('#result').fadeIn(500);
                $('#result').html('Result: ' + data.label);
                $('#sol').fadeIn(500);
                $('#sol').html(data.solution);

                console.log('Success!');
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
            }
        });
    });

});
