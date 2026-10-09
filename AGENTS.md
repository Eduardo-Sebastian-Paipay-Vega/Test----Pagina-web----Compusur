# Alcance de esta biblioteca

Al diseñar, construir o exportar contenido de esta carpeta, lee `.agents/skills/compusur-odoo-design/SKILL.md`.

## Selección de skills

- Verificación de compatibilidad real/importación de la página actual: `.agents/skills/verificar-odoo/SKILL.md`. Diagnosticar y documentar sin publicar. Distinguir contrato local y capacidades de Odoo.

- Dirección visual habitual: `.agents/skills/frontend-design/SKILL.md`.
- Alternativa cuando se elija la variante para Codex: `.agents/skills/codex-frontend-design/SKILL.md`. Usa una dirección de diseño por tarea; no cargar ambas por defecto.
- Auditoría de UX/accesibilidad solicitada o revisión pertinente: `.agents/skills/web-design-guidelines/SKILL.md`.
- `.agents/skills/react-best-practices/SKILL.md` solo corresponde a React/Next.js en el alcance de una tarea. La biblioteca actual no los usa; no introducirlos para activar la skill.

Las entradas locales adaptadas son el punto de acceso; consulta sus originales o reglas adicionales solo cuando resulten relevantes. `docs/SKILLS.md` describe versiones, uso y alcance. Las preferencias estéticas de una skill no sustituyen decisiones del usuario ni los límites técnicos del proyecto.

Edita fuentes en `src/`; genera `preview/` y `dist/` con `scripts/project.py`. Este proyecto es una vista previa y biblioteca de diseño: sus comandos no deben conectarse con Odoo ni publicar contenido. Una solicitud posterior de implementación se trabaja con el contexto y autorización de esa solicitud, fuera de este generador local.

No pongas datos reales de inventario en `products.sample.json` sin distinguir su procedencia y fecha. Conserva precios, compra y disponibilidad en las funciones nativas de Odoo al integrar. Usa CSS limitado a `.cs-site`; comprueba el alcance de cualquier modificación en plantillas globales.

Antes de preparar un paquete o planificar una subida, lee `docs/COMPATIBILIDAD-ODOO.md`. No eludir `scripts/export_policy.py` para conseguir que se genere un ZIP. Si una solicitud requiere algo fuera de este contrato, explicar qué integración necesita y revisar el alcance antes de cambiar el generador. No llamar «listo para subir/publicar» a una validación local: falta verificar la adaptación en Odoo.
