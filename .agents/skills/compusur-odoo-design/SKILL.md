---
name: compusur-odoo-design
description: Editar la biblioteca local de diseño COMPUSUR y preparar bloques HTML y CSS para su adaptación a Odoo. Usar al trabajar en compusur-web; no aplica a administración general de Odoo ni habilita publicación.
---

# Diseño e integración COMPUSUR

La raíz del proyecto es la carpeta que contiene `compusur-web.code-workspace`. Identifícala ascendiendo desde esta habilidad; no dependas de una ruta absoluta de un equipo.

## Diseño local

- Edita `src/blocks/inicio.html`, `src/partials/`, `src/styles/` y `src/scripts/preview.js` según el área solicitada. `src/pages/index.html` compone la vista previa. `{{PRODUCTS}}` lo resuelve el generador; no es sintaxis QWeb.
- `src/data/products.sample.json` contiene tres muestras procedentes del inicio auditado. Solo el enlace de la HP está identificado como ficha verificada. Los otros accesos abren el catálogo y su rótulo debe indicarlo. No inventes URLs de fichas ni precios para completar tarjetas.
- Mantén estilos dentro de `.cs-site`. La búsqueda, el carrito y la consulta de esta vista previa son demostraciones locales, sin envíos ni API. No añadir claves a fuentes, configuración de VS Code ni paquetes.
- Para revisar, usa `python scripts/project.py preview`; después de editar, reconstruye con `python scripts/project.py build`. La revisión visual debe cubrir escritorio y móvil, incluyendo lectura, acciones y ausencia de desbordamiento.

## Preparar para Odoo

Lee `docs/ODOO.md` al exportar o planificar integración. Ejecuta `python scripts/project.py check` después de cambiar el exportador, el contenido exportable o los recursos. El ZIP es un paquete de diseño en borrador, no un módulo instalable ni una importación de productos.

Consulta [el contrato de compatibilidad](../../../docs/COMPATIBILIDAD-ODOO.md). `export` valida obligatoriamente el contenido antes de generar el paquete. No quitar esa comprobación para incluir frameworks, código de servidor, controles de demostración, CSS global o recursos no portables. Para una función fuera del contrato, preparar una integración específica según la solicitud; no suponer que será importable por subir los archivos. La compatibilidad final sigue pendiente hasta revisar el resultado dentro de Odoo.

La conexión existente corresponde a COMPUSUR, sitio 1; la base tiene otro sitio. Al implementar una solicitud autorizada, identificar las vistas efectivas e inherited views del sitio objetivo, respaldar sus campos y verificar el resultado público. Una página sin publicar no aísla cambios en cabeceras o CSS globales.

Precios, stock, búsqueda comercial y compra deben conectarse a Odoo, en lugar de convertir la muestra estática en una segunda base de datos. El destino del formulario de cotización debe comprobarse antes de anunciar recepción de consultas. No exportes el JavaScript de demostración como lógica comercial.

## Contenido comercial

Consulta `docs/CONTENIDO.md` cuando un cambio afecte a contactos, envíos, pagos o Perú Compras. Las decisiones pendientes no se resuelven inventando datos. No es necesario bloquear cambios visuales independientes de esos datos.
