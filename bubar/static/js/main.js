$(document).ready(function() {

    $("#gas_form").find("input").each(function(){
        $(this).attr("name", $(this).attr("id"));
    });

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
        var input_value = $(this).find("input").val();
        for (var k in params.data ){
            $("#"+params.data[k]).val(input_value);
            $("#"+params.data[k]).text(input_value);
        }
    }

    $("#cal_dp").click(function (){
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "/bubar/gas" ,
            data: $('#gas_form').serialize(),
            success: function (result) {
                $("#c_33_9").text(result['dp1']);
                $("#c_46_12").text(result['dp1']);
                $("#c_33_12").text(result['dp2']);
                $("#c_49_12").text(result['bbb']);

                $("#c_34_9").text(result['dp1']*0.03);
                $("#c_35_9").text(result['pipe_id']*10);
                $("#c_49_12").text(result['time']);
            },
            error : function(err) {
                console.log(err);
                alert(err.responseText);
            }
        });
    });

    $("#cal_qv").click(function (){
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "/bubar/gas_qv" ,
            data: $('#gas_form').serialize(),
            success: function (result) {
                $("#c_47_12").text(result['qv']);
            },
            error : function(err) {
                console.log(err);
                alert(err.responseText);
            }
        });
    });

    // 数据同步到form 表单中
    $("#c_0_4").on("focusout",{ele_id: "project_name"}, focusoutHandler) ;
    $("#c_1_12").on("focusout",{ele_id: "operator"}, focusoutHandler) ;
    $("#c_2_12").on("focusout",{ele_id: "page"}, focusoutHandler) ;
    $("#c_4_12").on("focusout",{ele_id: "fluid"}, focusoutHandler) ;
    $("#c_5_9").on("focusout",{ele_id: "tag_number"}, focusoutHandler) ;

    $("#c_7_9").on("focusout",{ele_id: "pipe_od"}, focusoutHandler) ;
    $("#c_7_12").on("focusout",{ele_id: "c_39_12", ele_id2: "pipe_id"}, focusoutHandler) ;
    $("#c_8_9").on("focusout",{ele_id: "pipe_material"}, focusoutHandler) ;
    $("#c_8_12").on("focusout",{ele_id: "pipe_direction"}, focusoutHandler) ;
    $("#c_10_9").on("focusout",{ele_id: "c_42_12", ele_id2: "pf"}, focusoutHandler) ;
    $("#c_11_9").on("focusout",{ele_id: "c_41_12", ele_id2: "tf"}, focusoutHandler) ;
    $("#c_13_7").on("focusout",{ele_id: "c_32_12", ele_id2: "flow_rate_min"}, focusoutHandler) ;
    $("#c_13_9").on("focusout",{ele_id: "flow_rate_nor"}, focusoutHandler) ;
    $("#c_13_11").on("focusout",{ele_id: "flow_rate_max"}, focusoutHandler) ;
    $("#c_13_14").on("focusout",{ele_id1: "c_32_9", ele_id2: "c_45_12", ele_id3: "flow_rate_c"}, focusoutHandler) ;
    $("#c_17_9").on("focusout",{ele_id: "c_40_12", ele_id2: "mw"}, focusoutHandler) ;
    $("#c_18_9").on("focusout",{ele_id: "c_43_12", ele_id2: "tb"}, focusoutHandler) ;
    $("#c_18_12").on("focusout",{ele_id: "c_44_12", ele_id2: "pb"}, focusoutHandler) ;
    $("#c_22_9").on("focusout",{ele_id: "c_25_12", ele_id2: "press_rating"}, focusoutHandler) ;
    $("#c_28_9").on("focusout",{ele_id: "pipe_orientation"}, focusoutHandler) ;
    $("#c_28_12").on("focusout",{ele_id: "dp_conn_type"}, focusoutHandler) ;
    $("#c_47_9").on("focusout",{ele_id: "dp"}, focusoutHandler) ;

});