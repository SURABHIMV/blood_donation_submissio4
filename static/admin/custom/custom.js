function donar_data(id){

    var url ="view_donar";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
    
            success: function (data) {

                console.log(id)
                console.log(data)
                $("#donar_details_div").html(data.rendered_template);
                $("#donar_details_modal").modal("show");
            }

          });
}

$(document).ready(function() {
   
    $('#donar_form').submit(function(event) {
        console.log('jjjjjjjjjjjjjjj');

        event.preventDefault(); // Prevent the form from submitting normally

        // Clear previous error messages
        $('.error-message').text('');
        var form_data = new FormData($('#donar_form')[0]);
        // Collect form data
        var name = $('#name').val().trim();
        var nationality = $('#nationality').val().trim();
        var phone = $('#phone').val().trim();
        var age = $('#age').val().trim();
        var sex = $('#sex').val().trim();
        var email = $('#email').val().trim();
        var address = $('#address').val().trim();
        var date_of_donation = $('#date_of_donation').val().trim();
        var last_date_of_donation = $('#last_date_of_donation').val().trim();
        var donation = $('#donation').val().trim();
        // var donar_status = $('#donar_status').val().trim();
        var volume = $('#volume').val().trim();
        var hemoglobin = $('#hemoglobin').val().trim();
        var weight = $('#weight').val().trim();
        var medical_history = $('#medical_history').val().trim();
        var overall_health = $('#overall_health').val().trim();
        var image = $('#image').val().trim();
        var blood_type = $('#blood_type').val().trim(); // Fix the missing blood_type

        var hasError = false;
        console.log(name);
        // Validate fields
        if (!name) {
            $('#error-name').text('Name cannot be empty.');
            hasError = true;
        }
        if (!nationality) {
            $('#error-nationality').text('Nationality cannot be empty.');
            hasError = true;
        }
        if (!phone) {
            $('#error-phone').text('Phone cannot be empty.');
            hasError = true;
        }
        if (!age) {
            $('#error-age').text('Age cannot be empty.');
            hasError = true;
        }
        if (!sex) {
            $('#error-sex').text('Sex cannot be empty.');
            hasError = true;
        }
        if (!address) {
            $('#error-address').text('Address cannot be empty.');
            hasError = true;
        }
        if (!blood_type) {
            $('#error-blood_type').text('Blood type cannot be empty.'); // Fix error message target
            hasError = true;
        }
        if (!volume) {
            $('#error-volume').text('Volume cannot be empty.');
            hasError = true;
        }
        if (!hemoglobin) {
            $('#error-hemoglobin').text('Hemoglobin cannot be empty.');
            hasError = true;
        }
        if (!weight) {
            $('#error-weight').text('Weight cannot be empty.');
            hasError = true;
        }
        if (!medical_history) {
            $('#error-medical_history').text('Medical history cannot be empty.');
            hasError = true;
        }
        if (!overall_health) {
            $('#error-overall_health').text('Overall health cannot be empty.');
            hasError = true;
        }
        if (!image) {
            $('#error-image').text('Image cannot be empty.');
            hasError = true;
        }
        if (!email) {
            $('#error-email').text('Email cannot be empty.');
            hasError = true;
        }

        if (!date_of_donation) {
            $('#error-date_of_donation').text('date cannot be empty.');
            hasError = true;
        }

        if (!last_date_of_donation) {
            $('#error-last_date_of_donation').text('last date cannot be empty.');
            hasError = true;
        }

        if (!donation) {
            $('#error-donation').text('donation cannot be empty.');
            hasError = true;
        }

        if (!blood_type) {
            $('#error-blood-type').text('blood_type cannot be empty.');
            hasError = true;
        }

        // if (!donar_status) {
        //     $('#error-donar_status').text(' donar_status cannot be empty.');
        //     hasError = true;
        // }

        // if the flag hasError is true  then the form will not be submitted elsemove to ajax part

        if (hasError) {
            return; 
        }

        $.ajax({
            type: 'POST',
            url: "create_donar",
            data: form_data,
            processData: false,
            contentType: false,
            success: function(data) {
                status = data['status'];
                message = data['message'];

                if (status == "success") {
                    console.log('yyyyyyyyyyyyyyyyyyyyyyy');
                    // alert("Form submission successful!"+data.success);
                    // to refresh the page automatically
                    // $(document).ajaxStop(function(){
                    //     setTimeout("window.location = 'Blog'",100);
                    //   });
                    $('#donar_form').trigger('reset');
                    $(document).ajaxStop(function() {
                        setTimeout("window.location = ''", 100);
                    });

                    var toastMixin = Swal.mixin({
                        toast: true,
                        icon: status,
                        title: 'General Title',
                        animation: false,
                        position: 'top-right',
                        showConfirmButton: false,
                        timer: 3000,
                        timerProgressBar: true,
                        didOpen: (toast) => {
                            toast.addEventListener('mouseenter', Swal.stopTimer);
                            toast.addEventListener('mouseleave', Swal.resumeTimer);
                        }
                    });
                    toastMixin.fire({
                        animation: true,
                        title: message
                    });
                } else {
                    var toastMixin = Swal.mixin({
                        toast: true,
                        icon: status,
                        title: 'General Title',
                        animation: false,
                        position: 'top-right',
                        showConfirmButton: false,
                        timer: 3000,
                        timerProgressBar: true,
                        didOpen: (toast) => {
                            toast.addEventListener('mouseenter', Swal.stopTimer);
                            toast.addEventListener('mouseleave', Swal.resumeTimer);
                        }
                    });
                    toastMixin.fire({
                        animation: true,
                        title: message
                    });
                }
            }
        });
    });
});


function edit_entry(id){

    var url ="edit_donar";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
    
            success: function (data) {

                console.log(id)
                console.log(data)
                
                $("#edit_donar_details_div").html(data.rendered_template);
                $("#edit_details_modal").modal("show");
            }

          });
}

function edit_donar_action(){
    event.preventDefault()
    var form_data = new FormData($('#donar_edit_form')[0]);
    console.log('form_data')
    $.ajax({
        type: 'POST',
        url: "edit_donar_actionn",
        data: form_data,
        processData: false,
        contentType: false,
        success: function(data)
        {
            console.log('sssssssssssssssssssssssss')

        }
    })

}
