# Revisión local de compatibilidad con Odoo

Fecha y hora de Lima: 2026-10-09T12:02:20-05:00

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
- `src/assets/COMPUSUR.png`
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

## Revisión manual del diseño y del logo

Esta sección amplía el diagnóstico automático con comprobaciones locales y consultas de lectura a Odoo realizadas en esta ejecución. No se regeneró dist, no se corrigieron fuentes ni se modificó la tienda.

### Evidencia local actual

- `COMPUSUR.png`: PNG de 1448 × 417 píxeles, 145.329 bytes. El archivo de origen coincide byte a byte con preview, dist y ZIP; su SHA-256 coincide con el manifiesto.
- La cabecera usa `assets/media/COMPUSUR.png`, texto alternativo descriptivo y enlace a inicio. CSS fija ancho de 260 px en escritorio y 210 px en móvil, con altura automática. Esto demuestra la intención de conservar proporciones; no sustituye la revisión renderizada.
- HTML y CSS exportados coinciden con las fuentes actuales mediante `prepare_export()` en memoria, normalizando saltos de línea. Los archivos del ZIP coinciden con dist y sus huellas son correctas.
- ZIP: 147.367 bytes; contiene fragmento, CSS, PNG y manifiesto. Son tamaños locales, no una medición de rendimiento.
- La página local `preview/odoo.html` contiene el fragmento exportable exacto. Ese fragmento no referencia el PNG: el logo pertenece a la cabecera, que está excluida de la exportación. El recurso se transporta en el ZIP para su adaptación separada.
- Las correcciones anteriores se conservan: `styles()` combina exclusivamente las fuentes CSS; categorías y cabecera del catálogo admiten enlaces y botones; las acciones de producto comparten `cs-product-link`. Ya no se añade el bloque antiguo que sobrescribía el diseño.
- El manifiesto aún incluye «Logotipo original» en `unresolved`; es una descripción desactualizada de la disponibilidad del archivo. Debe distinguir «archivo incorporado» de «integración del logo en la cabecera de Odoo pendiente». No impide validar el paquete.
- Los documentos de contenido y prueba que aún indican ausencia del logo también requieren actualizar ese pendiente; siguen faltando las fotografías de productos.
- Búsqueda, carrito y cotización siguen siendo demostraciones en `preview.js`. La exportación excluye ese JavaScript, cabecera y pie; transforma acciones del inicio en enlaces a `/shop`, categorías y `/contactus`. El pie local contiene rótulos, no enlaces funcionales.
- No se detectan nuevas dependencias externas en las fuentes examinadas; los recursos del paquete son locales. Los estilos permanecen limitados a `.cs-site`.

### Comprobaciones de Odoo de esta ejecución

Evidencia de lectura guardada en [odoo-evidencia-logo.json](odoo-evidencia-logo.json).

- Sitio 1: COMPUSUR, `https://www.compusur.pe`.
- Módulos instalados: base `saas~19.3.1.3`, website `saas~19.3.1.0`, website_sale `saas~19.3.1.1`. Confirma la serie SaaS 19.3; no certifica el plan de alojamiento ni permisos de edición.
- HP, product.template 10: publicada y con URL configurada coincidente con la muestra. No se comprobó navegación pública, precio, stock ni compra.
- Inicio 593 activo del sitio 1; layout 596 compartido, heredado de 541; cabecera 5504 y pie 3506 activos del sitio 1, heredados de 596. No se obtuvo en esta ejecución el render combinado ni se validó toda la cadena de herencias o el editor.
- No se comprobó que este PNG esté cargado o asignado como logo en Odoo. La prueba privada de imagen 7707 descrita en docs/IMAGENES-ODOO.md no es el logo comercial y no prueba su integración.

### Revisión visual

El inventario de navegadores conectados volvió vacío. No se ejecutaron pruebas visuales de escritorio, tablet o móvil ni de teclado, zoom y desbordamiento. La inspección del CSS no demuestra esos resultados.

### Matriz de integración

| Elemento | Destino de integración | Estado | Evidencia | Corrección pendiente |
|---|---|---|---|---|
| Logo local | Recurso autorizado para cabecera | Preparado como borrador | PNG presente, dimensiones y SHA verificados; cabecera local lo referencia | Actualizar pendientes documentales |
| Logo en la tienda | Configuración del logo del sitio 1 y su cabecera efectiva 5504 | Pendiente de verificación en Odoo | Vista identificada; no hay comprobación de carga/asignación de este PNG | Confirmar mecanismo/campo, cargar o reutilizar recurso y verificar representación |
| Inicio | Bloque de contenido de website.homepage 593, o página de prueba aislada | Preparado como borrador | Contrato local aprobado; dist coincide con fuentes | Probar inserción y edición dentro del tema |
| CSS | Recurso asociado al destino y limitado a .cs-site | Preparado como borrador | Estilos unificados; sin sobreescritura antigua del exportador | Probar cascada efectiva, tamaños y accesibilidad |
| Cabecera y pie | Vistas del sitio 1, 5504 y 3506, y sus herencias | Pendiente de verificación en Odoo | Excluidos del fragmento de inicio | Adaptación separada y comprobación del layout compartido |
| Ficha HP, registro y ruta | product.template 10 | Verificado en Odoo | Lectura actual confirma publicación y URL | Verificar página pública, características y datos comerciales |
| Fotos y muestras ASUS/DesignJet | Imágenes y fichas del catálogo nativo | Pendiente de verificación en Odoo | Fotografías ausentes; muestras enlazan /shop | Identificar productos y confirmar información |
| Búsqueda, stock, precios y compra | Funciones nativas de website_sale | Pendiente de verificación en Odoo | Módulo instalado; controles locales simulados | Conectar y probar recorridos reales |
| Cotización | /contactus y receptor de su formulario | Pendiente de verificación en Odoo | Enlace exportado; sin envío local | Confirmar destino y recepción |
| Paquete | Traslado del borrador y PNG | Preparado como borrador | ZIP y huellas coincidentes | No equivale a instalación ni publicación |
| Presentación adaptable | Vista completa, fragmento y página integrada | Pendiente de verificación en Odoo | Sin navegador disponible | Revisar escritorio, tablet, móvil, foco, zoom y desbordamiento |

### Conclusión

No hay bloqueos del contrato local. El nuevo logo está incorporado a la propuesta y al paquete, pero su aparición en Odoo requiere integrar la cabecera por separado. Se detectó un pendiente documental desactualizado; no se corrigió por tratarse de una auditoría. La tienda aún necesita fotografías, datos y funciones comerciales nativas y pruebas visuales/funcionales.

Siguiente acción concreta: actualizar el estado documental del logo y preparar su asignación al sitio 1 con verificación del destino de cabecera, antes de ejecutar una integración real autorizada. Mantener separados la disponibilidad del archivo, su carga en Odoo y su visualización pública.
