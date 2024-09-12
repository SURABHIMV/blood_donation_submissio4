function u_data(id){

    var url ="view_u";
            $.ajax({
            url: url,
            data: {
              'id': id
            },
            
    
            success: function (data) {

                console.log(id)
                console.log(data)
                $("#u_details_div").html(data.rendered_template);
                $("#u_details_modal").modal("show");
            }

          });
}

function addtomail(id){

  var url ="addmail";
          $.ajax({
          url: url,
          data: {
            'id': id
          },
         
          success: function(data)
          {
            status = data['status']
            message = data['message']
            
           
            if (status == "success"){
                // alert("Form submission successful!"+data.success);
                // to refresh the page automaticaly
                // $(document).ajaxStop(function(){
                //     setTimeout("window.location = 'Blog'",100);
                //   });
                console.log(status)
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
        
        
        });
}
