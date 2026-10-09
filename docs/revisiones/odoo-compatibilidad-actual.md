# Revisión local de compatibilidad con Odoo

Fecha y hora de Lima: 2026-10-09T11:37:55-05:00

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
- `src/pages/odoo-preview.html`
- `src/partials/footer.html`
- `src/partials/header.html`
- `src/scripts/preview.js`
- `src/styles/site.css`
- `src/styles/tokens.css`

## Revisi?n manual despu?s de las correcciones

Se retiraron los estilos antiguos a?adidos por el exportador. Las categor?as usan las reglas de src/styles/site.css tanto como botones como enlaces. Las acciones de producto comparten cs-product-link y las reglas de la cabecera del cat?logo admiten ambos elementos. CSS de origen es ahora la ?nica fuente de presentaci?n del paquete.

La nueva prueba local preview/odoo.html contiene el fragmento exportable exacto, sin JavaScript de demostraci?n. Su aviso superior no se exporta. Los enlaces /shop y /contactus requieren Odoo. No se cre? una p?gina de prueba en Odoo.

Las seis pruebas del contrato y project.py check pasaron despu?s de los cambios. No se ha efectuado revisi?n visual en navegador. Foco, responsive y desbordamiento siguen pendientes de prueba renderizada.

### Matriz actual

| Elemento | Destino de integraci?n | Estado | Evidencia | Correcci?n pendiente |
|---|---|---|---|---|
| Inicio y CSS | Bloque de p?gina del sitio 1 y recurso CSS limitado a .cs-site | Preparado como borrador | Contrato aprobado; estilos unificados | Revisar aspecto y carga en tema real |
| Fragmento de prueba | preview/odoo.html; despu?s p?gina aislada en Odoo | Preparado como borrador | Generado desde prepare_export; sin simulaciones | Ejecutar gu?a de prueba |
| Cabecera y pie | Vistas del sitio 1: 5504 y 3506, seg?n lectura previa | Pendiente de verificaci?n en Odoo | Excluidos del ZIP | Revisar cadena efectiva y adaptaci?n separada |
| Cat?logo y compra | Funciones nativas website_sale | Pendiente de verificaci?n en Odoo | Solo muestras y mensajes en vista previa | Vincular datos y probar recorrido |
| Im?genes y marca | Adjuntos y campos de producto | Pendiente de verificaci?n en Odoo | No hay im?genes locales | A?adir originales autorizados |
| Cotizaci?n | /contactus y receptor real | Pendiente de verificaci?n en Odoo | Enlace exportado; no env?o local | Probar destino y recepci?n |
| Sitio, m?dulos, ficha HP y categor?as | Registros de Odoo | Verificado en Odoo | Consulta de lectura de la auditor?a previa del 9 de octubre, conservada en JSON | No implica prueba de UI ni compra; reconfirmar al integrar |

La evidencia de Odoo de la auditor?a anterior se conserva en previous_odoo_read_evidence del JSON. No se repitieron esas consultas en esta correcci?n. El alcance de aquella evidencia se limita a registros: sitio 1, m?dulos SaaS 19.3, HP publicada con URL coincidente, categor?as 9/10/17 y vistas identificadas; no certifica edici?n, alojamiento, render ni funcionamiento comercial.

Siguiente acci?n: seguir [la gu?a de prueba](../PRUEBA-INTEGRACION-ODOO.md), comenzando por revisi?n visual local y comprobaci?n de aislamiento/recursos en el destino. No hay bloqueos del contrato local; la integraci?n y publicaci?n contin?an pendientes.
