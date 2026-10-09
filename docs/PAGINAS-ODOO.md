# Verificación para agregar páginas en Odoo

## Borradores locales de páginas

La biblioteca genera esqueletos de vista previa en `preview/paginas/` a partir de `src/data/pages.sample.json`. También crea alias locales: `/catalogo/`, `/producto/`, `/cotizacion/`, `/nosotros/`, `/servicios/`, `/peru-compras/` y `/privacidad/`. La cabecera y el pie enlazan las pantallas; el inicio está en `/index.html`. Se pueden abrir en `http://127.0.0.1:8767/` cuando el servidor local se haya iniciado en ese puerto.

La vista previa también presenta una respuesta local HTTP 404. La posibilidad y el alcance de esa configuración en Odoo constan en [PROTOCOLO-ENLACE-INEXISTENTE.md](PROTOCOLO-ENLACE-INEXISTENTE.md).

Los enlaces entre archivos son navegación de la vista previa. La etiqueta “Destino previsto en Odoo” es una referencia de integración, no una redirección configurada. No crear ni modificar redirecciones, registros, menús o páginas en Odoo al regenerar estos archivos. La exportación de producción sigue limitada al bloque de inicio hasta que el generador se amplíe deliberadamente.

Podemos diseñar páginas nuevas en esta biblioteca y adaptarlas a Odoo. Crear un archivo local no crea una página en Odoo. El generador actual exporta únicamente el bloque de inicio; para exportar otras páginas hay que ampliar la selección y validación del generador según el alcance solicitado.

## Evidencia aportada

La captura del usuario muestra títulos y rutas de páginas existentes. No muestra sitio, identificadores de registros, permisos, publicación, visibilidad ni indexación. No usarla como inventario completo o comprobación actual de la conexión.

Rutas visibles: `/`, `/about-us`, `/acerca-de`, `/catalogo-peru-compras`, `/contactus`, `/contactus-thank-you`, `/job-thank-you`, `/our-services`, `/pricing`, `/privacy`, `/your-task-has-been-submitted` y `/your-ticket-has-been-submitted`.

“Sobre nosotros” y “Acerca de” podrían repetir contenido; comparar su contenido y uso antes de consolidar. Las páginas de agradecimiento o recepción pueden estar vinculadas a formularios y aplicaciones: verificar esos vínculos antes de cambiarlas. La ausencia de `/shop` en esta captura no significa que no exista: las páginas dinámicas se gestionan de otra forma.

## Antes de diseñar o crear

1. Definir objetivo, título, contenido y acción del cliente. Determinar si corresponde a una página informativa nueva o a una función nativa existente.
2. Comprobar el sitio objetivo en el entorno actual. La referencia previa es COMPUSUR, sitio 1, pero debe confirmarse al implementar.
3. Leer el inventario actual de páginas, menús y redirecciones. Elegir una ruta que no colisione con páginas, rutas dinámicas o redirecciones existentes; no basta revisar esta captura.
4. Revisar contenido similar antes de duplicarlo. No reemplazar la portada, contacto, privacidad ni páginas de respuesta de formularios por suposición.
5. Identificar el destino real de cada bloque, imagen y acción. Aplicar `COMPATIBILIDAD-ODOO.md`; conectar catálogo, compra y consultas a funciones nativas. No subir el ZIP como si fuera un módulo instalable.
6. Comprobar con lectura la disponibilidad de herramientas y permisos de páginas, vistas, menús y adjuntos. El MCP general está configurado en lectura y el MCP de imágenes solo carga recursos: ninguno demuestra autorización técnica para crear páginas. Registrar esa capacidad como pendiente hasta verificarla.

## Al implementar una página autorizada

1. Respaldar los registros que se modificarán y registrar sus identificadores, sitio, ruta y estado. Preparar una página sin publicar, sin añadirla al menú público durante la prueba.
2. Usar contenido y estilos propios de la página; revisar el alcance de vistas heredadas y recursos compartidos. Una página sin publicar no aísla cambios en CSS, cabecera o pie globales.
3. Sustituir rutas locales de imágenes por recursos de Odoo. Un adjunto privado no se vuelve visible al visitante por insertarlo en HTML; comprobar acceso según el uso autorizado.
4. Configurar por separado publicación, visibilidad, menú e indexación. Una página publicada puede no aparecer en el menú. No tratar una URL poco conocida o la desindexación como control de acceso.
5. Verificar título SEO, descripción, idioma, enlaces, imágenes, lectura y navegación en escritorio y móvil. Probar los formularios y su recepción solo cuando esa operación esté autorizada.
6. Antes de publicar, registrar pendientes y el resultado dentro de Odoo. Al publicar según la solicitud, comprobar el dominio público sin sesión. Si se cambia una URL existente, revisar enlaces y preparar la redirección correspondiente.

## Registro por página

Documentar: objetivo, título, URL, sitio confirmado, fuente local, destino de integración, registros afectados, publicación/visibilidad/indexación deseadas, recursos, acciones, respaldo y evidencia de pruebas. Usar los estados de `verificar-odoo`: borrador local, pendiente en Odoo, bloqueo concreto o elemento verificado en Odoo.

Referencia oficial: [Gestión de páginas en Odoo SaaS 19.3](https://www.odoo.com/documentation/saas-19.3/applications/websites/website/structure/pages.html).
