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

    function focusoutHandler(params){
        var val = $(this).find("input").val();
        for (var k in params.data ){
//            alert(k+" "+params.data[k]);
            $("#"+params.data[k]).text(val);
        }
    }

    $("#c_7_12").on("focusout",{ele_id: "c_39_12"}, focusoutHandler) ;
    $("#c_10_9").on("focusout",{ele_id: "c_42_12"}, focusoutHandler) ;
    $("#c_11_9").on("focusout",{ele_id: "c_41_12"}, focusoutHandler) ;
    $("#c_13_7").on("focusout",{ele_id: "c_32_12"}, focusoutHandler) ;
    $("#c_13_14").on("focusout",{ele_id1: "c_32_9", ele_id2: "c_45_12"}, focusoutHandler) ;
    $("#c_17_9").on("focusout",{ele_id: "c_40_12"}, focusoutHandler) ;
    $("#c_18_9").on("focusout",{ele_id: "c_43_12"}, focusoutHandler) ;
    $("#c_18_12").on("focusout",{ele_id: "c_44_12"}, focusoutHandler) ;
    $("#c_22_9").on("focusout",{ele_id: "c_25_12"}, focusoutHandler) ;
});