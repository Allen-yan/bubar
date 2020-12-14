$(document).ready(function() {

    // double click made to edit form
    $("#sheet0").on("dblclick", "td", function() {
        if ($(this).children("input").length>0 ||  !$(this).hasClass("editable")) {
            return false;
        }
        var td_dom=$(this);
        //Save the initial value
        var td_init_value=$(this).text();
        //Set width for td and set width for input and assign value
        $(this).width(100).html("<input type=\"text\">").find("input").width(100).val(td_init_value);
        //Reassign when focus is lost
        var input_dom=$(this).find("input");
        input_dom.blur(function() {
          // revert td form
          var new_text=$(this).val();
          $(this).remove();
          td_dom.text(new_text);


       });
    });


});