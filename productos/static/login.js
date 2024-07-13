$(document).ready(function() {
    $("#bEnviar").click(function() {
        var nombre = $("#itNombre").val();
        var password = $("#itPassword").val();

        if (nombre == "") {
            $("#mensaje1").fadeIn();
            return false;  // Evita que se envíe el formulario si el nombre está vacío
        } else {
            $("#mensaje1").fadeOut();
            if (password == "") {
                $("#mensaje2").fadeIn();
                return false;  // Evita que se envíe el formulario si la contraseña está vacía
            } else {
                $("#mensaje2").fadeOut();
                // Aquí podrías agregar más validaciones si fuera necesario
            }
        }
    });
});
