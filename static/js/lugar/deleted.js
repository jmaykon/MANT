document.addEventListener("click", async function (e) {
    const btn = e.target.closest(".btn-eliminar");
    if (!btn) return;

    e.preventDefault();
    const url = btn.dataset.url;

    // Confirmación con SweetAlert2
    const result = await Swal.fire({
        title: "¿Estás seguro?",
        text: "Este lugar será eliminado permanentemente.",
        icon: "warning",
        draggable: true,
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
        confirmButtonColor: "#dc2626",
        cancelButtonColor: "#6b7280"
    });

    if (result.isConfirmed) {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
            });

            if (response.ok) {
                await Swal.fire({
                    title: "Eliminado 🗑️",
                    text: "El lugar fue eliminado correctamente.",
                    icon: "success",
                    draggable: true,
                    confirmButtonColor: "#2563eb"
                });

                // Recargar lista de lugares con HTMX
                htmx.ajax('GET', '/lugar/', { target: '#dynamic-content', swap: 'innerHTML' });
            } else {
                throw new Error("Error al eliminar");
            }
        } catch (error) {
            Swal.fire({
                title: "Error",
                text: "No se pudo eliminar el lugar.",
                icon: "error",
                draggable: true,
                confirmButtonColor: "#ef4444"
            });
        }
    }
});
