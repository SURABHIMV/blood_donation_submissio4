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
          
  
          success: function (data) {

              console.log(id)
              console.log(data)
             
          }
        
        });
}
