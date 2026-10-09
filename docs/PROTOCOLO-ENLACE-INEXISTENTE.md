# Protocolo para enlaces inexistentes

## Comportamiento esperado

1. Responder con **HTTP 404** cuando la ruta realmente no existe.
2. Mostrar en español “No encontramos esta página”, una explicación breve y accesos al inicio, catálogo y contacto.
3. Mostrar la ruta solicitada solo como texto escapado; no interpretar su contenido como HTML ni reflejar parámetros de consulta.
4. Mantener el estado 404 aunque la página ofrezca navegación. No enviar toda URL desconocida al inicio.
5. Si una ruta antigua tiene un reemplazo concreto, crear una regla específica: 301 permanente, 302 temporal, 308 para reescritura permanente de una ruta dinámica o 404 cuando una ruta concreta se retire sin reemplazo.
6. Corregir el origen de enlaces internos rotos. Usar una redirección solo cuando la antigua URL aún recibe visitas o enlaces externos.

## Comprobación en COMPUSUR Odoo

Consulta de solo lectura a COMPUSUR, sitio 1, el 9 de octubre de 2026:

- Está disponible el modelo `website.rewrite`. Sus campos incluyen `url_from`, `url_to`, `redirect_type`, `website_id` y `active`; admite los tipos `404`, `301`, `302` y `308`.
- La búsqueda de reglas de reescritura no encontró registros. Odoo ya maneja con su 404 predeterminado una ruta desconocida; no hace falta crear una regla para cada enlace mal escrito.
- La plantilla QWeb `http_routing.404` (vista 499) y el wrapper `website.page_404` (vista 712) están activos. La plantilla compartida muestra texto en inglés y enlaces a `/contactus` e inicio.
- La vista 499 no tiene un sitio asignado, por tanto es global. La vista 713 (`website.404_plausible`) hereda de ella para registrar el evento en Plausible cuando está configurado. Una personalización debe preservar esa herencia y evitar afectar el otro sitio.
- La búsqueda de `/404` en `website.page` no devolvió una página estática. El 404 es una plantilla atendida por Odoo.

La documentación oficial confirma que se pueden administrar redirecciones en **Website ‣ Configuration ‣ Redirects**, que una URL inexistente sin redirección conserva el estado 404 y que las páginas pueden personalizarse. [Páginas y redirecciones en Odoo SaaS 19.3](https://www.odoo.com/documentation/saas-19.3/applications/websites/website/structure/pages.html).

**Conclusión:** Odoo soporta el protocolo. Las redirecciones se configuran para rutas concretas. Una página 404 con identidad COMPUSUR también es técnicamente viable mediante la plantilla QWeb existente; hay que comprobar en una copia o entorno de prueba que el editor de Odoo Online permita aplicarla solo a COMPUSUR. La plantilla actual es global, así que no editarla directamente en producción sin revisar su alcance y la integración Plausible.

## Prototipo local

`src/pages/404.html` y `PreviewHandler` muestran el mensaje, la dirección solicitada escapada y los enlaces útiles, manteniendo HTTP 404. Para probar en local, inicia `python scripts/project.py preview --port 8767` y visita `http://127.0.0.1:8767/enlace-que-no-existe`. Esta demostración no ha cambiado Odoo.

## Al implementar en Odoo

1. Probar la adaptación de la vista 404 en un duplicado/entorno de pruebas o con una herencia limitada al sitio COMPUSUR.
2. Conservar la herencia de Plausible, si sigue habilitada.
3. Probar una URL inexistente y otra retirada mediante regla; ambas deben responder HTTP 404 con opciones claras de navegación.
4. Añadir redirecciones individuales solo para URLs anteriores con destino aprobado; revisar el sitio asociado y evitar cadenas.
5. No publicar hasta comprobar que rutas existentes, como catálogo y contacto, conservan su respuesta normal.

No se modificaron páginas, reglas, vistas ni permisos en Odoo durante esta comprobación.
