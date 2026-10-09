# Alcance de esta biblioteca

El estilo común está establecido en `docs/ESTILO-VISUAL.md` (Tienda editorial tecnológica). Leerlo antes de diseñar o modificar pantallas; mantener coherencia con `src/styles/tokens.css`. Cambiar esta dirección cuando la solicitud del usuario lo requiera y actualizar la referencia, sin inventar un estilo independiente por página.

Para estructura del sitio, páginas nuevas o coherencia entre pantallas, usar `.agents/skills/diseno-integral-odoo/SKILL.md` y mantener `docs/DISENO-INTEGRAL.md` como referencia de decisiones. Coordinar skills por necesidad; no cargar todas ni abrir subagentes por el mero hecho de orquestar el diseño.

Antes de proponer, crear o integrar páginas nuevas, leer `docs/PAGINAS-ODOO.md` y aplicar sus verificaciones. La lista de páginas de una captura no prueba permisos, publicación ni compatibilidad; comprobar el sitio y las rutas actuales en Odoo al implementar.

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

Para una carga de imágenes autorizada, leer `docs/IMAGENES-ODOO.md` y usar el MCP específico `odoo_compusur_images` o su comando documentado. Son operaciones de carga real, separadas del generador local. Mantener `public=false` salvo que la solicitud incluya hacer accesible ese recurso para la web. No habilitar escritura genérica para cargar un banner. La prueba privada 7707 no debe insertarse ni publicarse como contenido comercial.
