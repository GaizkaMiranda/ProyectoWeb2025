const API_URL_DETALLE_EMPLEADO = "http://127.0.0.1:8000/api/empleado/";

// Espera a que el DOM cargue completamente
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".detalle-empleado").forEach(item => {
        item.addEventListener("click", function (e) {
            e.preventDefault(); // evita que el enlace recargue la página

            const li = this.closest(".item-lista");

            const nombre = li.dataset.nombre;
            const disponibilidad = li.dataset.disponibilidad || "No especificada";
            const telefono = li.dataset.telefono || "No especificado";

            // Actualiza el contenido del contenedor de detalles
            document.getElementById("detalle-nombre").textContent = nombre;
            document.getElementById("detalle-disponibilidad").textContent = disponibilidad;
            document.getElementById("detalle-telefono").textContent = telefono;

            // Muestra el contenedor si está oculto
            document.getElementById("detalles-empleado").style.display = "block";
        });
    });
});


function cargarDetalleEmpleado(id) {
    const apiUrl = `${API_URL_DETALLE_EMPLEADO}${id}/`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error("Error al cargar los datos del empleado.");
            }
            return response.json();
        })
        .then(data => {
            mostrarDetalleEnDOM(data);
        })
        .catch(error => {
            console.error(error);
            document.getElementById("detalles-empleado").innerHTML = `
                <div class="error">⚠️ No se pudo cargar la información del empleado.</div>`;
        });
}

function mostrarDetalleEnDOM(empleado) {
    const contenedor = document.getElementById("detalles-empleado");

    contenedor.innerHTML = `
        <div class="detalle-box">
            <h3>Detalles del empleado</h3>
            <p><strong>Nombre:</strong> ${empleado.nombre} ${empleado.apellido}</p>
            <p><strong>Puesto:</strong> ${empleado.puesto}</p>
            <p><strong>Email:</strong> ${empleado.email}</p>
            <p><strong>Disponibilidad:</strong> ${empleado.disponibilidad}</p>
        </div>
    `;

    contenedor.style.display = "block";
}
