# Límite de diseño y exportación

Este documento delimita lo que prepara la biblioteca para el sitio COMPUSUR de Odoo Online. Es el contrato de nuestro generador; no afirma que Odoo prohíba universalmente todas las tecnologías que quedan fuera del paquete.

| Contenido | Decisión para esta biblioteca |
|---|---|
| Bloques HTML estáticos, enlaces y CSS dentro de `.cs-site` | Admitidos en el borrador; adaptar y comprobar en el tema real |
| Imágenes/fuentes locales autorizadas | Admitidas si sus archivos están en el paquete; reasignar recursos en Odoo |
| Catálogo, precios, stock y compra | Conectar con funciones de Odoo; las muestras no sustituyen datos reales |
| Cabecera, pie y JavaScript de la vista previa | No incluidos en esta exportación de inicio |
| React/Next.js, JSX, SSR, Node.js, Python y archivos de entorno | Fuera del paquete de diseño; no subir como si fueran bloques de Odoo Online |
| Script, iframe, formulario nuevo, control local o QWeb sin adaptar | El exportador los rechaza; requieren una integración específica revisada |
| CSS global, imports y enlaces de recursos a CDN o rutas del equipo | El exportador los rechaza para mantener este borrador independiente y limitado |
| Claves, skills, documentación y herramientas del proyecto | No forman parte del ZIP; el paquete se construye con una selección explícita de archivos |
| ZIP generado | Paquete de traslado de un borrador; no es un módulo instalable ni una publicación |

## Comprobación obligatoria

`python scripts/project.py export` y `check` ejecutan `scripts/export_policy.py` antes de escribir el fragmento, CSS o ZIP. Rechazan los elementos indicados, recursos ausentes y tipos de archivo no previstos. Si falla esa comprobación, no se reemplaza el ZIP anterior: ese archivo conserva su versión anterior y no representa los cambios rechazados.

La política admite HTML/CSS y recursos estáticos. No es un antivirus ni un analizador completo de todas las variantes de HTML/CSS. No certifica permisos, editor, herencias del tema, sanitización de Odoo, rendimiento real ni recepción de consultas.

Pruebas de los límites:

```powershell
python -m unittest discover -s tests -v
```

## Antes de subir o publicar

1. Identificar dónde se integrará cada bloque en las vistas efectivas de COMPUSUR, sitio 1.
2. Respaldar los registros afectados y preparar una prueba sin alterar vistas globales de producción.
3. Cargar recursos y conectar datos/comportamientos a Odoo; no publicar las muestras como catálogo definitivo.
4. Comprobar el resultado dentro de Odoo y en móvil, además de los recorridos comerciales afectados.

El manifiesto registra `odoo_compatibility: pending-in-odoo-review`. Ese estado expresa que todavía falta la prueba dentro de Odoo, incluso cuando las comprobaciones locales pasan.
