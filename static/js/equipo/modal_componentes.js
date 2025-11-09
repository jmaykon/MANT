function openModal(addComponenteModal) {
    const modal = document.getElementById(addComponenteModal);
    modal.classList.remove('hidden');
    modal.classList.add('flex');
}

function closeModal(addComponenteModal) {
    const modal = document.getElementById(addComponenteModal);
    modal.classList.add('hidden');
    modal.classList.remove('flex');
}