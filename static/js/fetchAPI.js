const API_URL_DETALLE_EMPLEADO = "http://127.0.0.1:8000/api/empleado/";

// Espera a que el DOM cargue completamente
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".detalle-empleado").forEach(item => {
        item.addEventListener("click", function (e) {
            e.preventDefault(); // evita que el enlace recargue la página

            const li = this.closest(".item-lista");

            const nombre = li.dataset.nombre;
            const dni = li.dataset.dni || "No especificado";
            const apellidos = li.dataset.apellidos || "No especificado";
            const disponibilidad = li.dataset.disponibilidad || "No especificada";
            const email = li.dataset.email || "No especificado";
            const telefono = li.dataset.telefono || "No especificado";

            // Actualiza el contenido del contenedor de detalles
            document.getElementById("detalle-nombre").textContent = nombre;
            document.getElementById("detalle-dni").textContent = dni;
            document.getElementById("detalle-apellidos").textContent = apellidos;
            document.getElementById("detalle-email").textContent = email;
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
            <p><strong>Nombre:</strong> ${empleado.nombre}</p>
            <p><strong>Apellido:</strong> ${empleado.apellidos}</p>
            <p><strong>Email:</strong> ${empleado.email}</p>
            <p><strong>Disponibilidad:</strong> ${empleado.disponibilidad}</p>
        </div>
    `;

    contenedor.style.display = "block";
}
