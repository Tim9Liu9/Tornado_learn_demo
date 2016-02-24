
//$(document).ready(function(){
//    alert("good4");
//    $("#login").click(function(){
//        var user = $("#username").val();
//        var pwd = $("#password").val();
//        alert("username: "+user);
//    });
//});


function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        //var pd = {"username":user, "password":pwd};
        // xsrf
         var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                //alert(data);
                window.location.href = "/user?user="+data;
            },
            error:function(){
                alert("error!");
            },
        });
    });
});