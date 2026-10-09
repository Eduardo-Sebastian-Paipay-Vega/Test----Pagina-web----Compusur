# Alcance de esta biblioteca

Al diseñar, construir o exportar contenido de esta carpeta, lee `.agents/skills/compusur-odoo-design/SKILL.md`.

Edita fuentes en `src/`; genera `preview/` y `dist/` con `scripts/project.py`. Este proyecto es una vista previa y biblioteca de diseño: sus comandos no deben conectarse con Odoo ni publicar contenido. Una solicitud posterior de implementación se trabaja con el contexto y autorización de esa solicitud, fuera de este generador local.

No pongas datos reales de inventario en `products.sample.json` sin distinguir su procedencia y fecha. Conserva precios, compra y disponibilidad en las funciones nativas de Odoo al integrar. Usa CSS limitado a `.cs-site`; comprueba el alcance de cualquier modificación en plantillas globales.
