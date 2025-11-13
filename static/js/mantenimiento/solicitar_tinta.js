document.getElementById('tipo_soporte').addEventListener('change', function () {
    const coloresDiv = document.getElementById('colores_tinta');

    // Si el usuario selecciona "Recarga de Tinta", mostramos el bloque
    if (this.value === 'recarga_tinta') {
        coloresDiv.classList.remove('hidden');
    } else {
        coloresDiv.classList.add('hidden');
        // Limpia los checkboxes al ocultar
        coloresDiv.querySelectorAll('input[type="checkbox"]').forEach(chk => chk.checked = false);
    }

    // Agregar lógica de exclusión para "Todos" y colores individuales
    const checkboxes = coloresDiv.querySelectorAll('input[type="checkbox"]');
    const todos = coloresDiv.querySelector('input[value="todos"]');

    checkboxes.forEach(chk => {
        chk.addEventListener('change', function () {
            if (this.value === 'todos') {
                if (this.checked) {
                    checkboxes.forEach(c => { if (c.value !== 'todos') c.checked = false; });
                }
            } else {
                if (this.checked) {
                    todos.checked = false;
                }
            }
        });
    });
});
