document.addEventListener("DOMContentLoaded", function () {
    const aumentarTexto = document.getElementById("aumentarTexto");
    const disminuirTexto = document.getElementById("disminuirTexto");

    let fontSize = 16;

    function cambiarTamanoTexto(tamano) {
        const elementos = document.querySelectorAll("h1, h2, h3, h4, h5, h6, p, li, td, th");
        elementos.forEach(el => {
            el.style.fontSize = tamano + "px";
        });
    }

    if (aumentarTexto) {
        aumentarTexto.addEventListener("click", function (e) {
            e.preventDefault();
            fontSize += 1;
            cambiarTamanoTexto(fontSize);
        });
    }

    if (disminuirTexto) {
        disminuirTexto.addEventListener("click", function (e) {
            e.preventDefault();
            fontSize -= 1;
            cambiarTamanoTexto(fontSize);
        });
    }
});
