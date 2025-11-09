
document.body.addEventListener('htmx:configRequest', (event) => {
    const tokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
    if (tokenInput) {
        const token = tokenInput.value;
        event.detail.headers['X-CSRFToken'] = token;
    }
});
