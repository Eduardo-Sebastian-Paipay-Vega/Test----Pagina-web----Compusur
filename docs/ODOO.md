# Adaptación a Odoo

La instalación auditada es Odoo SaaS 19.3. El sitio objetivo es COMPUSUR, `website_id=1`. El tema tiene personalizaciones QWeb y vistas heredadas. Las seis correcciones aplicadas anteriormente no autorizan por sí solas la publicación de este nuevo diseño.

## Lo que entrega esta biblioteca

- `dist/odoo/inicio.fragment.html`: contenido de inicio, sin documento HTML completo, cabecera global, formularios ni scripts.
- `dist/odoo/compusur.css`: estilos limitados a `.cs-site`.
- `dist/odoo/assets/media/`: recursos autorizados, cuando se añadan.
- `dist/odoo/manifest.json`: estado de borrador, limitaciones y huellas SHA-256.
- `dist/compusur-diseno-borrador.zip`: esos archivos para traslado y revisión.

El ZIP no se instala como módulo en Odoo Online y no se importa como CSV/XLSX. «Importable» significa que el contenido está separado para adaptarlo a los bloques y vistas disponibles del sitio. La forma concreta de inserción debe comprobarse con el editor y permisos actuales. No se afirma que basta subir el ZIP para publicar.

## Pasos de integración

1. Seleccionar los bloques revisados y confirmar el contenido comercial que utilicen.
2. Leer la plantilla efectiva y sus herencias; distinguir contenido de página, cabecera, ficha y CSS global. Respaldar los registros afectados y sus recursos.
3. Preparar el contenido en una página sin publicar o en un entorno de prueba disponible. Evitar que la prueba cambie vistas globales de la web activa.
4. Cargar recursos y sustituir rutas locales por los recursos de Odoo. Conservar el logotipo original.
5. Convertir las tarjetas estáticas en bloques vinculados al catálogo real. Los precios, imágenes y stock deben obtenerse de Odoo. Adaptar búsqueda y carrito a sus funciones nativas.
6. Confirmar y probar el destino de cotización: formulario de contacto, correo o CRM según el flujo elegido. No habilitar todos a la vez por suposición.
7. Verificar escritorio/móvil, navegación, accesibilidad y rendimiento antes/después. Publicar el cambio revisado y comprobar el dominio público.

El generador no crea plantillas QWeb instalables porque aún no se han elegido las vistas de integración. No incluye conexión de producción ni intenta activar escritura en el MCP.

## Recursos

Guarda imágenes autorizadas en `src/assets/`. El generador las copia a `assets/media/`. En una fuente, utiliza esa ruta para la vista previa; al integrar, cambia la ruta al adjunto correspondiente de Odoo. El paquete admite imágenes y fuentes, pero no ejecutables ni documentos de clientes.

Las fuentes y el ZIP deben inspeccionarse antes de traslado. La validación local es estructural; no valida la procedencia de todos los recursos ni sustituye la prueba funcional dentro de Odoo.
