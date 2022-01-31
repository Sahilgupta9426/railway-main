$(function () {
  
  

    /* Functions */
    
    $( document ).ready(function() {
      var btn = $(this);
      $.ajax({
        url: "{% url 'searchform' %}",
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-train .modal-content").html("");
          $("#modal-train").modal("show");
        },
        success: function (data) {
          $("#modal-train .modal-content").html(data.html_form);
        }
      });
    });
    
    var showdata = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#train-table tbody").html(data.html_train_list);
            $("#modal-train").modal("hide");
            $(".showhide").show();
          }
          else {
            $("#modal-train .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    
    };
    var getcutomer = function () {
      var btn = $(this);
      console.log("hello")
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#customer").html("");
          console.log("hello")
         
        },
        success: function (data) {
          $(".showhide").hide();
          $("#customer").html(data.html_form);
          
          console.log("hello")
        }
      });
    };
    
    // for cutomer get loading 
     
    //end customer
    
    /* Binding */
    
    // Create book
    
    $("#modal-train").on("submit", ".js-book-create-form", showdata);
    $(".showhide").hide();
    $("#customerID").click(getcutomer)
    });
    