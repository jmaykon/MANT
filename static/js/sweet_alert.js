// ==============================
// Función de toast personalizado
// ==============================
function alertaToast(type, mensaje) {
    Swal.fire({
        position: "top-end",
        icon: type,
        title: mensaje,
        showConfirmButton: false,
        timer: 1500,
        toast: true,
        timerProgressBar: true
    });
}

// ==============================
// Función para confirmar eliminación con HTMX
// ==============================
function confirmarEliminar(btn) {
    Swal.fire({
        title: "¿Eliminar lugar?",
        text: "Esta acción no se puede deshacer",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6"
    }).then((result) => {
        if (result.isConfirmed) {
            alertaToast("success", "Lugar eliminado");

            // Ejecuta hx-delete manualmente con CSRF
            htmx.ajax('DELETE', btn.dataset.url, {
                target: btn.getAttribute('hx-target'),
                headers: { "X-CSRFToken": obtenerCSRF() }
            });
        }
    });
}

// ==============================
// Función para alerta de agregado
// ==============================
function alertaAgregado() {
    Swal.fire({
        title: "¡OK!",
        text: "Lugar Agregado Correctamente!",
        icon: "success"
    });
}
function alertaEliminado() {
    Swal.fire({
        title: "¡OK!",
        text: "Lugar Eliminado Correctamente!",
        icon: "success"
    });
}

// ==============================
// Función para obtener CSRF
// ==============================
function obtenerCSRF() {
    return document.querySelector('meta[name="csrf-token"]').content;
}

// ==============================
// Listeners
// ==============================

// Captura clicks en botones eliminar
document.addEventListener("click", function (e) {
    const btn = e.target.closest(".btn-eliminar");
    if (!btn) return;
    e.preventDefault();
    confirmarEliminar(btn);
});

// HTMX: alerta después de agregar lugar
document.addEventListener("htmx:afterRequest", (e) => {
    if (e.detail.requestConfig.verb === "post") {
        alertaAgregado();
    }
});

// Configura CSRF para todos los requests HTMX
document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = obtenerCSRF();
});
