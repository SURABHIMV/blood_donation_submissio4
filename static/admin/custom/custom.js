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


