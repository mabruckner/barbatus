$(function(){
    $("body").append($("<table>"));
    var options = ["null","Bill","Bob","Jeb"];
    for(var i=0;i<3;i++){
        var row=$("<tr>");
        for(var j=0;j<3;j++){
            var cell=$("<td>");
            var selection=$("<select>");
            for(var n=0;n<options.length;n++){
                option=$("<option>");
                option.attr("value",options[n]);
                option.text(options[n]);
                //selection.change(function(){console.log("hello");});
                selection.append(option);
            }
            selection.attr("x",j);
            selection.attr("y",i);
            //selection.change);});
            cell.append(selection);
            row.append(cell);
        }
        $("table").append(row);
    }
    $("select").change(function(thing){
        var $sel = $(thing.target);
        console.log($(thing.target).attr("x"));
        var move=JSON.stringify({"x":parseInt($sel.attr("x")),"y":parseInt($sel.attr("y"))});
        console.log(move);
        $.get("/rest/asdf",{"player":"Bob","move":move});
    });
});
