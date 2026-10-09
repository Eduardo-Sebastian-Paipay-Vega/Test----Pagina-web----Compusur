# Prueba del inicio COMPUSUR

Estado: preparación local. No se creó una página ni se modificaron vistas en Odoo.

## Archivos y revisión local

Ejecuta `python scripts/project.py preview` y abre:

- `http://127.0.0.1:8767/`: propuesta completa con controles de demostración.
- `http://127.0.0.1:8767/odoo.html`: HTML exportable exacto con enlaces, sin cabecera, pie ni JavaScript de demostración.

La segunda página conserva `/shop`, categorías y `/contactus`; esas rutas requieren Odoo y no funcionan en el servidor local. Su propósito es revisar presentación y foco de los enlaces. El contenedor informativo superior pertenece a la prueba y no se incluye en el ZIP.

`python scripts/project.py check` genera y valida el paquete actual en `dist/compusur-diseno-borrador.zip`. Contiene el fragmento, CSS y manifiesto. No es un módulo instalable.

## Destino previsto y aislamiento

La lectura de Odoo del 9 de octubre de 2026 identificó COMPUSUR, sitio 1, inicio `website.homepage` 593 y layout compartido 596. Cabecera 5504 y pie 3506 son vistas del sitio 1. Volver a comprobar estos datos al ejecutar la prueba.

1. Preferir una copia de prueba del sitio/base. Si se usa una página nueva sin publicar del sitio 1, comprobar sus permisos de acceso: no publicarla no equivale a un entorno aislado.
2. Respaldar los campos de cualquier registro que vaya a modificarse y registrar IDs de recursos nuevos. Definir restauración antes de aplicar cambios.
3. Insertar `dist/odoo/inicio.fragment.html` dentro del contenedor de contenido de la página de prueba, sin reemplazar el inicio 593 ni duplicar el layout.
4. Cargar `dist/odoo/compusur.css` mediante un mecanismo confirmado para esa página. No modificar bundles compartidos o cabecera/pie para una prueba de contenido. Si el editor no permite limitar el recurso, usar la copia de prueba antes de continuar.
5. Conservar el envoltorio `.cs-site`. Reasignar imágenes autorizadas a adjuntos de Odoo cuando estén disponibles. Las muestras actuales no son el catálogo definitivo.

## Criterios de aceptación

| Área | Comprobación necesaria | Estado |
|---|---|---|
| Presentación | Comparar vista completa y fragmento en 1440, 768, 390 y 320 px; sin desbordamiento ni textos cortados | Pendiente de navegador |
| Interacción accesible | Recorrer enlaces por Tab/Shift+Tab, foco visible y activación por Enter; revisar zoom al 200 % | Pendiente |
| Tema real | Verificar CSS calculado y herencias; no alterar páginas ajenas a la prueba | Pendiente en Odoo |
| Categorías | Abrir los destinos de Laptops, Computadoras y Monitor con el contexto del sitio 1 | Pendiente en Odoo |
| Productos | Confirmar ficha HP y resolver fichas ASUS/DesignJet; sustituir tarjetas estáticas por catálogo nativo | Pendiente en Odoo |
| Recursos | Incorporar logotipo original y fotografías correspondientes a cada producto | Pendiente |
| Comercio | Probar búsqueda, precios, disponibilidad, carrito y checkout nativos con un recorrido de prueba | Pendiente en Odoo |
| Cotizaciones | Confirmar `/contactus`, campos, destino y recepción con una consulta de prueba identificada | Pendiente en Odoo |

La preparación local no publica contenido. Registrar capturas, resultados y registros afectados durante la prueba real antes de decidir la implementación definitiva.
