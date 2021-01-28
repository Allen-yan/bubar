$(document).ready(function() {
    $("#steam_form").find("input").each(function(){
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
    function elementLoadHandler(params){
        var input_value = $(this).text();
        for (var k in params.data ){
            $("#"+params.data[k]).val(input_value);
            $("#"+params.data[k]).text(input_value);
        }
    }


    function handle_success_form(payload, if_commit){
        // 加载页面各元素
        if(payload){
            // 其它元素
            if (!if_commit){
                // 隐藏input元素
                $("#project_name").val(payload['project_name']);
                $("#operator").val(payload['operator']);
                $("#page").val(payload['page']);
                $("#fluid").val(payload['fluid']);
                $("#tag_number").val(payload['tag_number']);
                $("#pipe_od").val(payload['pipe_od']);
                $("#pipe_id").val(payload['pipe_id']);
                $("#pipe_material").val(payload['pipe_material']);
                $("#pipe_direction").val(payload['pipe_direction']);
                $("#pf").val(payload['pf']);
                $("#tf").val(payload['tf']);
                $("#flow_rate_min").val(payload['flow_rate_min']);
                $("#flow_rate_nor").val(payload['flow_rate_nor']);
                $("#flow_rate_max").val(payload['flow_rate_max']);
                $("#flow_rate_c").val(payload['flow_rate_c']);
                $("#od").val(payload['od']);
                $("#press_rating").val(payload['press_rating']);
                $("#pipe_orientation").val(payload['pipe_orientation']);
                $("#dp_conn_type").val(payload['dp_conn_type']);
                $("#dp").val(payload['dp']);

                // 显示元素
                $("#c_0_4").text(payload['project_name']);
                $("#c_1_12").text(payload['operator']);
                $("#c_2_12").text(payload['page']);
                $("#c_4_12").text(payload['fluid']);
                $("#c_5_9").text(payload['tag_number']);
                $("#c_7_9").text(payload['pipe_od']);
                $("#c_7_12").text(payload['pipe_id']);
                $("#c_39_12").text(payload['pipe_id']);
                $("#c_8_9").text(payload['pipe_material']);
                $("#c_8_12").text(payload['pipe_direction']);
                $("#c_10_9").text(payload['pf']);
                $("#c_11_9").text(payload['tf']);
                $("#c_41_12").text(payload['tf']);
                $("#c_13_7").text(payload['flow_rate_min']);
                $("#c_32_12").text(payload['flow_rate_min']);
                $("#c_13_9").text(payload['flow_rate_nor']);
                $("#c_13_11").text(payload['flow_rate_max']);
                $("#c_13_14").text(payload['flow_rate_c']);
                $("#c_32_9").text(payload['flow_rate_c']);
                $("#c_41_12").text(payload['flow_rate_c']);
                $("#c_14_9").text(payload['od']);
                $("#c_40_12").text(payload['od']);
                $("#c_18_9").text(payload['tb']);
//                $("#c_43_12").text(payload['tb']);
//                $("#c_18_12").text(payload['pb']);
//                $("#c_44_12").text(payload['pb']);
                $("#c_22_9").text(payload['press_rating']);
                $("#c_25_12").text(payload['press_rating']);
                $("#c_28_9").text(payload['pipe_orientation']);
                $("#c_28_12").text(payload['dp_conn_type']);
                $("#c_47_9").text(payload['dp']);
            }
            $("#c_33_9").text(payload['dp1']);
            $("#c_46_12").text(payload['dp1']);
            $("#c_33_12").text(payload['dp2']);
            $("#c_38_12").text(payload['flow_factor']);

            $("#c_34_9").text(payload['dp1']*0.03);
            $("#c_35_9").text(payload['pipe_id']*10);
            $("#c_49_12").text(payload['create_time']);

        }
    }

    //初始化时加载已有数据
    handle_success_form(init_data, false);
    $("#cal_dp").click(function (){
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "/bubar/steam" ,
            data: $('#steam_form').serialize(),
            success: function (result) {
//                handle_success_form(result, true);
                  window.location = "/bubar/steam?id=" + result["id"];

            },
            error : function(err) {
                console.log(err);
                alert(err.responseText);
            }
        });
    });

    $("#cal_qm").click(function (){
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "/bubar/steam_qm" ,
            data: $('#steam_form').serialize(),
            success: function (result) {
                $("#c_47_12").text(result['qm']);
            },
            error : function(err) {
                console.log(err);
                alert(err.responseText);
            }
        });
    });

    // 数据同步到form 表单中
    $("#c_0_4").on("focusout",{ele_id: "project_name"}, focusoutHandler).on("change", {ele_id: "project_name"}, elementLoadHandler);
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
    $("#c_13_14").on("focusout",{ele_id1: "c_32_9", ele_id2: "c_41_12", ele_id3: "flow_rate_c"}, focusoutHandler) ;
    $("#c_14_9").on("focusout",{ele_id: "c_40_12", ele_id2: "od"}, focusoutHandler) ;
    $("#c_18_9").on("focusout",{ele_id: "c_43_12", ele_id2: "tb"}, focusoutHandler) ;
    $("#c_18_12").on("focusout",{ele_id: "c_44_12", ele_id2: "pb"}, focusoutHandler) ;
    $("#c_22_9").on("focusout",{ele_id: "c_25_12", ele_id2: "press_rating"}, focusoutHandler) ;
    $("#c_28_9").on("focusout",{ele_id: "pipe_orientation"}, focusoutHandler) ;
    $("#c_28_12").on("focusout",{ele_id: "dp_conn_type"}, focusoutHandler) ;
    $("#c_47_9").on("focusout",{ele_id: "dp"}, focusoutHandler) ;

});