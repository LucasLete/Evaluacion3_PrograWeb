$(document).ready(function() {
    $("#bEnviar").click(function() {
        var nombre = $("#itNombre").val();
        var password = $("#itPassword").val();

        if (nombre == "") {
            $("#mensaje1").fadeIn();
            return false;
        }else{
            $("#mensaje1").fadeOut();
            if(password == "") {
                $("#mensaje2").fadeIn();
                return false;

            }
        }
    });
});
