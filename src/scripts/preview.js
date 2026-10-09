/* Interacciones locales: no crea pedidos, envía formularios ni usa la API. */
(() => {
  const root = document.getElementById('compusur-preview');
  if (!root) return;
  const search = root.querySelector('input[type="search"]');
  const cards = [...root.querySelectorAll('[data-product]')];
  const result = root.querySelector('.cs-result');
  const feedback = root.querySelector('.cs-feedback');
  let category = 'Todos';

  function filter() {
    const query = search.value.trim().toLocaleLowerCase('es');
    let count = 0;
    cards.forEach(card => {
      const visible = (category === 'Todos' || card.dataset.category === category)
        && card.textContent.toLocaleLowerCase('es').includes(query);
      card.hidden = !visible;
      if (visible) count += 1;
    });
    result.textContent = count ? `${count} ${count === 1 ? 'producto' : 'productos'} de muestra · ${category}` : 'No hay una muestra de esta categoría o búsqueda.';
    root.querySelectorAll('[data-filter]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.filter === category));
    });
  }

  function show(message) {
    feedback.hidden = false;
    feedback.textContent = message;
    feedback.scrollIntoView({block: 'nearest', behavior: 'auto'});
  }

  root.querySelectorAll('[data-filter]').forEach(button => {
    button.addEventListener('click', () => {
      category = button.dataset.filter;
      filter();
      root.querySelector('#catalogo').scrollIntoView({block: 'start', behavior: 'auto'});
    });
  });
  root.querySelectorAll('[data-action]').forEach(button => {
    button.addEventListener('click', () => show(button.dataset.action === 'quote'
      ? 'Cotización propuesta: uso, cantidad, presupuesto y contacto. Esta vista previa no envía consultas.'
      : 'Carrito de demostración vacío. El carrito real seguirá conectado a Odoo.'));
  });
  root.querySelectorAll('[data-details]').forEach(button => {
    button.addEventListener('click', () => show(`${button.dataset.details}: acceso previsto ${button.dataset.url}. Precio y disponibilidad deben consultarse en Odoo.`));
  });
  search.addEventListener('input', filter);
  filter();
})();
