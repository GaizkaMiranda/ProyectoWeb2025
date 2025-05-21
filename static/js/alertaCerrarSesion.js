// Captura de evento en DOM y mostar alerta si el usuario pulsa "cerrar sesion"
// Se trata de una implementacion que trata de asegurarse mediante una doble confirmacion 
// de que el usuario, efectivamente quiere cerrar sesion

document.addEventListener("DOMContentLoaded", function () {
    const cerrarSesion = document.getElementById("cerrarSesion");

    if (cerrarSesion) {
        cerrarSesion.addEventListener("click", function (e) {
            const confirmado = confirm("¿Confirmar cierre de sesión?");
            if (!confirmado) {
                e.preventDefault(); // Cancela la redirección si el usuario pulsa "Cancelar"
            }
        });
    }
});
