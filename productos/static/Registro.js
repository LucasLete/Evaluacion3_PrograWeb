var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+.[a-zA-Z0-9\-\.]+$/;
    $(document).ready(function(){
        $("#bEnviar").click(function(){
            var nombre = $("#itNombre").val();
            var mail = $("#itMail").val();
            var password = $("#itPassword").val();
            
            if (nombre == ""){
                $("#mensaje1").fadeIn();
                return false;
            }else{
                $("#mensaje1").fadeOut();
                if (mail == "" || !expr.test($("#itMail").val())){
                    $("#mensaje2").fadeIn();
                    return false;
                }else{
                    $("#mensaje2").fadeOut();
                    if (password == ""){
                        $("#mensaje3").fadeIn();
                        return false;
                    }
                }
            }
        });
    });