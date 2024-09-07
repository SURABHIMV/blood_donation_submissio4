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

function create_submit(){
  event.preventDefault()
  var form_data = new FormData($('#donar_form')[0]);
  console.log("donar_form");
  // Log form data to console for debugging
  // for (var pair of form_data.entries()) {
  // console.log(pair[0]+ ': ' + pair[1]); 
  // }


  // alert("SS"+form_data)
  // console.log("gggggg"+form_data)

  $.ajax({
      type: 'POST',
      url: "create_donar",
      data: form_data,
      processData: false,
      contentType: false,
      success: function(data)
      {
        status = data['status']
        message = data['message']
        
        alert("SS"+message)
        if (status == "success"){
            console.log('jjjjjjjjjjjjjjjjjjjjj')
            // alert("Form submission successful!"+data.success);
            // to refresh the page automaticaly
            // $(document).ajaxStop(function(){
            //     setTimeout("window.location = 'Blog'",100);
            //   });
            $('#donar_form').trigger('reset'); 
            $(document).ajaxStop(function(){
                setTimeout("window.location = ''",100);
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
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
            });
            toastMixin.fire({
            animation: true,
            title: message
            });
        }
        else{
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
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
            });
            toastMixin.fire({
            animation: true,
            title: message
            });
            
        }

    }
      // {
      //     status = data['status']
      //     message = data['message']
      //     da=data['data']
      //     $('#donar_form')[0].reset();
 
      //     // alert("SS"+message)
      //     if (status == "success"){
             
      //         console.log(da['id'])
              
      //     }

      // }
  })

}


