# Biblioteca web de COMPUSUR

Proyecto local para editar el diseño en Visual Studio Code y preparar bloques revisables para Odoo. No contiene credenciales ni funciones de publicación automática.

Abre `compusur-web.code-workspace` en Visual Studio Code. Requisito: Python 3.10 o posterior; no es necesario instalar paquetes, Node.js ni extensiones para estos comandos.

## Empezar

Desde la terminal situada en esta carpeta:

```powershell
python scripts/project.py preview
```

Abre `http://127.0.0.1:8767/`. Para detener el servidor, pulsa Ctrl+C. Después de editar las fuentes, ejecuta la tarea **Compusur: construir** y recarga el navegador. No edites `preview/` ni `dist/`: se generan a partir de `src/`.

También puedes usar **Terminal → Ejecutar tarea** en VS Code:

- Compusur: vista previa
- Compusur: construir
- Compusur: validar
- Compusur: exportar borrador Odoo

## Estructura

```text
src/
  pages/index.html           Página de la vista previa
  partials/                 Cabecera y pie de muestra
  blocks/inicio.html        Bloques que se adaptarán a Odoo
  styles/tokens.css         Colores y estilo base
  styles/site.css           Composición adaptable, limitada a .cs-site
  scripts/preview.js         Interacciones locales de demostración
  data/products.sample.json Productos de muestra, no inventario real
  assets/                   Logotipo, imágenes y fuentes autorizadas
scripts/project.py          Construcción, servidor, validación y exportación
docs/                       Límites de importación y contenido pendiente
.agents/skills/              Habilidad local para trabajar este proyecto
preview/                    Resultado generado para revisar
dist/odoo/                  Fragmento y CSS para adaptar a Odoo
dist/compusur-diseno-borrador.zip  Paquete de diseño, no módulo instalable
```

## Exportar y comprobar

```powershell
python scripts/project.py check
python scripts/project.py export
```

`check` reconstruye la vista previa y el paquete, comprueba el fragmento exportado y verifica las huellas de sus archivos. No acredita funcionamiento de precios, stock, pagos, formularios ni la compatibilidad final del tema: estas pruebas se realizan al integrar en Odoo.

La exportación incluye solo el contenido de inicio y CSS de alcance limitado. No reemplaza la cabecera global ni el carrito de Odoo. La búsqueda y los botones de demostración se excluyen; los accesos exportados utilizan enlaces locales a categorías o contacto. Las tarjetas son muestras estáticas y requieren sustitución por contenido real antes de publicar.

## Control de cambios

Esta carpeta pertenece al repositorio Git existente de `Proyecto oddo`. Las fuentes se pueden comparar y guardar en versiones desde VS Code; no se creó un segundo repositorio ni se hizo un commit. Los resultados generados están excluidos mediante `.gitignore`.

La habilidad local está en `.agents/skills/compusur-odoo-design/SKILL.md` y se referencia desde `AGENTS.md`. No se instaló una habilidad global ni se modificó la configuración de conexión. Puedes pedir a Codex que la use al trabajar en esta carpeta.

Consulta [integración en Odoo](docs/ODOO.md) antes de importar y [contenido pendiente](docs/CONTENIDO.md) antes de publicar.
