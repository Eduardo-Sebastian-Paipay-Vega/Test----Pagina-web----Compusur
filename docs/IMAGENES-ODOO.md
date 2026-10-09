# Imágenes para COMPUSUR y estado de carga

Verificación inicial y configuración realizada el 9 de octubre de 2026. La prueba posterior creó un adjunto privado; no se modificó ninguna página.

## Configuración activa

Se registró `odoo_compusur_images`, un MCP local que solo ofrece `upload_website_image`. El MCP general `odoo_compusur` conserva `READ_ONLY=true`. La clave cifrada existente se utiliza dentro del worker PowerShell; no se guarda en el proyecto ni se envía como argumento.

La herramienta admite archivos de `src/assets/` de hasta 5 MB en PNG, JPG/JPEG, WebP o SVG sin contenido activo. Su valor por defecto es `public=false`. `public=true` hace accesible ese recurso para la web y requiere que sea un recurso destinado a publicación; no publica ni modifica páginas. El servidor no edita productos ni reemplaza sus imágenes: esa integración queda fuera de esta herramienta.

Prueba real: adjunto **7707**, PNG privado de 2 × 2 píxeles y 73 bytes, asociado al sitio 1. Lectura posterior y SHA-256 coincidentes con el archivo local. PNG es el formato probado en esta ejecución; los demás deben comprobarse con sus archivos concretos. El recurso de prueba no se incluye en el paquete de diseño.

Registro de cargas: `odoo/media-registry.json`. La URL de un adjunto privado requiere acceso autorizado; no debe aparecer en una página pública hasta que se gestione su visibilidad mediante una operación específica.

### Usar después de reiniciar Codex

Pide cargar la imagen con `odoo_compusur_images.upload_website_image` indicando `file: "src/assets/nombre.png"` y `public: false` para una carga privada. No pasar claves ni datos binarios al modelo: la herramienta lee el archivo validado localmente.

También existe un comando de terminal:

```powershell
python scripts/odoo_images_mcp.py --upload src/assets/nombre.png
```

Este comando realiza una carga real privada. Añadir `--public` crea un recurso accesible para la web; no utilizarlo con archivos privados del negocio. Cada ejecución busca una carga previa equivalente en Odoo, lee el adjunto y verifica el binario para evitar duplicados y resultados basados solo en caché.

La configuración se registra con `scripts/configure_images_mcp.ps1`, que respalda config.toml y conserva las otras conexiones. Se siguió la [documentación oficial de MCP de Codex](https://developers.openai.com/codex/mcp).

## Resultado

- Odoo permite guardar imágenes y utilizarlas en páginas; la documentación oficial describe adjuntos y URLs `/web/image/...`.
- La clave de COMPUSUR declara permiso de creación en `ir.attachment` y de escritura en `product.template`. Los permisos de modelo no prueban por sí solos la carga sobre cada registro, su acceso público ni la asociación correcta al sitio.
- El puente MCP inicia y ofrece herramientas `create` y `write` con valores de campos. Su configuración actual contiene `READ_ONLY=true`: bloquea la carga de imágenes mientras permanezca así. No se habilitó escritura en esta verificación.
- Esta instancia expone `raw` y `db_datas` como campos binarios de adjuntos; la consulta no devuelve `datas`, usado por algunos ejemplos de Odoo 19.0. La carga debe adaptarse a los campos y serialización realmente disponibles, sin copiar un ejemplo de otra versión.
- `product.template.image_1920` está disponible como campo binario editable. No se sustituyó ninguna imagen de producto.

Evidencias de la consulta inicial del proyecto superior: `auditoria/verificacion-imagenes-actual.json` y `auditoria/verificacion-mcp-imagenes.json`. Para la prueba de carga posterior, consultar `odoo/media-registry.json`. La carga y lectura del adjunto están comprobadas; todavía falta su inserción y visualización en una página real.

## Flujo de diseño e integración

1. Guardar imágenes autorizadas en `src/assets/` y referenciarlas como `assets/media/nombre.jpg` en la propuesta. El exportador comprueba que el archivo exista y lo incluye en el paquete.
2. Para fotografías y banners, empezar con JPG o PNG. SVG puede utilizarse para un logotipo autorizado sin contenido activo. Otros formatos requieren comprobar el editor y la carga concreta; que una extensión esté admitida por nuestro paquete no prueba su aceptación en Odoo.
3. Al implementar una carga autorizada, usar el editor de Odoo o una conexión con escritura habilitada para esa operación. Subir y vincular cada recurso al destino/sitio adecuado; no usar rutas del equipo ni asumir que subir el ZIP carga automáticamente los adjuntos.
4. Probar primero una imagen en un contexto de borrador con el campo binario y método correctos. Verificar archivo, tipo, dimensiones, asociación y permisos de lectura; no hacer públicos adjuntos privados del negocio para solucionar una imagen que no carga.
5. Sustituir rutas de la vista previa por URLs de recursos de Odoo y comprobar el resultado en la página objetivo, escritorio y móvil. Las imágenes de productos se gestionan como datos del catálogo, no como reemplazos del tema.

Como orientación, la documentación propone reducir el peso —idealmente por debajo de 200 KB cuando la calidad lo permita— y no usar dimensiones innecesarias. Estas son recomendaciones de rendimiento, no límites duros de importación.

Fuente: [Media — documentación oficial de Odoo 19.0](https://www.odoo.com/documentation/19.0/developer/howtos/website_themes/media.html). La configuración viva de SaaS prevalece al elegir el campo y método de carga.
