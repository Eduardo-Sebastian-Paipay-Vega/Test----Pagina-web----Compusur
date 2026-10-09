# Revisión local de compatibilidad con Odoo

Fecha y hora de Lima: 2026-10-09T11:33:48-05:00

**Contrato local:** DRAFT_CONTRACT_PASSED

**Validación dentro de Odoo:** pendiente. **Listo para publicar:** no.

Fuentes locales actuales de compusur-web; no consulta la web publicada ni el backend.

Este diagnóstico evalúa el contrato del borrador. Un bloqueo no significa que Odoo prohíba esa tecnología en todas las instalaciones.

## Bloqueos detectados

No se detectaron bloqueos del contrato estático.

## Pendientes para una integración real

- Verificar características y destinos actuales de los productos de muestra; las verificaciones guardadas no son comprobaciones de esta ejecución.
- Completar imágenes reales: el inicio exportable todavía contiene marcadores de imagen.
- Probar inserción, recursos, permisos y herencias del tema dentro de Odoo, sitio COMPUSUR 1.
- Conectar precios, imágenes, stock, búsqueda y carrito a funciones nativas; las muestras son estáticas.
- Verificar destino y recepción real de cotizaciones; el prototipo no envía consultas.
- Confirmar datos comerciales pendientes antes de publicarlos.
- Revisar el resultado en escritorio, tablet y móvil; no se ejecutó revisión visual en este comando.
- Medir carga real y comportamiento de recursos dentro de Odoo; el tamaño local no demuestra velocidad.

## Código fuera de esta exportación

- `src/scripts/preview.js`

## Productos de muestra

- HP 15-GW0013LA: `/shop/tmvfm-portatil-hp-15-gw0013la-15-6-fhd-ryzen-7-3700u-10`; requiere comprobación actual en Odoo.
- ASUS TUF Gaming F16: `/shop`; requiere comprobación actual en Odoo.
- HP DesignJet T950: `/shop`; requiere comprobación actual en Odoo.

## Fuentes revisadas

Las huellas de la ejecución están en el informe JSON junto a este archivo.
- `src/assets/README.md`
- `src/blocks/inicio.html`
- `src/data/products.sample.json`
- `src/pages/index.html`
- `src/partials/footer.html`
- `src/partials/header.html`
- `src/scripts/preview.js`
- `src/styles/site.css`
- `src/styles/tokens.css`
