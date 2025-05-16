document.addEventListener('DOMContentLoaded', () => {
    const DNI = document.getElementById('id_dni');
    const email = document.getElementById('id_email');
    const telefono = document.getElementById('id_telefono');
    const mensajeDiv = document.getElementById('mensaje-validacion');
    const formulario = document.querySelector('form'); // Selección genérica del form

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    function showMessage(message) {
        mensajeDiv.innerText = message;
        mensajeDiv.style.display = 'block';
    }

    function clearMessage() {
        mensajeDiv.innerText = '';
        mensajeDiv.style.display = 'none';
    }

    DNI.addEventListener('blur', () => {
        if (DNI.value.length !== 9 && DNI.value.length !== 0) {
            showMessage('La longitud del DNI debe ser igual a 9');
        } else {
            clearMessage();
        }
    });

    telefono.addEventListener('blur', () => {
        if (telefono.value.length !== 9 && telefono.value.length !== 0) {
            showMessage('La longitud del teléfono debe ser igual a 9');
        } else {
            clearMessage();
        }
    });

    email.addEventListener('blur', () => {
        if (email.value.length > 0 && !emailRegex.test(email.value)) {
            showMessage('El formato del correo electrónico no es válido.');
        } else {
            clearMessage();
        }
    });

    formulario.addEventListener('submit', (event) => {
        if (DNI.value.length !== 9) {
            showMessage('La longitud del DNI debe ser igual a 9');
            event.preventDefault();
        } else if (telefono.value.length !== 9) {
            showMessage('La longitud del teléfono debe ser igual a 9');
            event.preventDefault();
        } else if (!emailRegex.test(email.value)) {
            showMessage('El formato del correo electrónico no es válido.');
            event.preventDefault();
        } else {
            clearMessage();
        }
    });
});

