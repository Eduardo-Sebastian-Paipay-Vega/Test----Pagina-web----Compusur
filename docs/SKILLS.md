# Skills de diseño instaladas

Instalación local del 9 de octubre de 2026 en `.agents/skills/`, dentro de `compusur-web`. No se modificaron las skills globales, la conexión MCP, permisos ni el diseño publicado.

| Invocación | Función en COMPUSUR | Uso |
|---|---|---|
| `$compusur-odoo-design` | Estructura, exportación y límites de integración | Base común al trabajar esta biblioteca |
| `$frontend-design` | Identidad visual, jerarquía, tipografía y contenido | Dirección visual habitual |
| `$codex-frontend-design` | Variante de composición y revisión visual para Codex | Alternativa al diseñador anterior |
| `$web-design-guidelines` | UX, accesibilidad, controles y presentación adaptable | Revisiones pertinentes o auditorías solicitadas |
| `$react-best-practices` | Rendimiento de React/Next.js | Solo cuando la tarea contenga esas tecnologías; no activa en el HTML/CSS actual |

Las cuatro skills solicitadas están descargadas. Las dos variantes de diseño no se ejecutan juntas por defecto: se elige la que corresponda. Las reglas detalladas de React se conservan como referencia y se cargan únicamente si aplican.

## Configuración para Odoo

- HTML/CSS de alcance `.cs-site` y JavaScript local mínimo; sin convertir la tienda en una aplicación React/Next.js.
- Fuente editable en `src/`, revisión en `preview/`, adaptación de salida desde `dist/odoo/`.
- Precios, stock, catálogo, búsqueda y compra mantienen sus conexiones nativas de Odoo al implementar.
- Los controles de demostración no se exportan como funciones comerciales. No se incluyen claves en archivos o ZIP.
- Sin promesas inventadas de descuentos, disponibilidad, atención, envíos o condiciones.
- Revisión de cambios sustanciales en escritorio, tablet y móvil. Las comprobaciones locales no sustituyen pruebas del formulario, pago o entrega dentro de Odoo.
- Instalar una skill no autoriza publicar ni cambiar permisos de Odoo.

## Procedencia y versiones

Se utilizó el instalador de skills de Codex con revisiones concretas, sin ejecutar scripts de los repositorios descargados. Una adaptación local reemplaza cada entrada `SKILL.md`; su original se conserva en `references/upstream-SKILL.md`.

- [Anthropic Frontend Design](https://github.com/anthropics/skills/tree/9d630808e4add0a7146de4af9384155d5dee350a/skills/frontend-design): licencia original en `LICENSE.txt`.
- [Variante Codex de dobromirdikov](https://github.com/dobromirdikov/codex-frontend-design-skill/tree/983119775a936d123df9fbfbc3821bdee5bb58fd/skills/frontend-design): renombrada localmente a `codex-frontend-design` para evitar colisión; licencia Apache-2.0 conservada en `LICENSE`.
- [Vercel Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines).
- [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices): la entrada original declara MIT; se conservaron documento compilado, metadatos y reglas.

El registro `.agents/skills/sources.lock.json` contiene revisiones y huellas SHA-256 de las entradas originales y de la adaptación inicial. También registra la versión de la copia local de las directrices de interfaz de Vercel. Una revisión con acceso a internet consulta su versión oficial actual; si usa la copia, debe indicar su fecha.

## Cómo usarlas

Abre esta carpeta como proyecto de Codex, o indica que debe trabajar dentro de ella y seguir su `AGENTS.md`. Las nuevas skills estarán disponibles para descubrimiento en el siguiente turno cuando este proyecto esté en el alcance de Codex; si la lista de la interfaz no se actualiza, abre una nueva sesión en `compusur-web`. Los archivos también pueden leerse directamente por su ruta.

Ejemplo:

> Usa frontend-design y las reglas compusur-odoo-design para mejorar el inicio. Conserva la integración con Odoo y revisa la experiencia móvil. Aplica web-design-guidelines a las áreas modificadas.

Para elegir la alternativa, sustituye `frontend-design` por `codex-frontend-design`. No es necesario añadir React Best Practices a este flujo.

## Mantenimiento

`python scripts/check_skills.py` verifica nombres únicos, referencias locales, originales y registro de procedencia sin usar paquetes externos. Las adaptaciones pueden editarse; el comprobador señala cuando su huella cambia respecto a la configuración inicial.

`scripts/configure_skills.py` conserva los originales y vuelve a generar las cuatro adaptaciones desde sus plantillas locales. No descarga versiones nuevas y puede reemplazar cambios manuales hechos en las entradas adaptadas; usarlo solo si se desea regenerarlas. Para actualizar desde GitHub, revisar y comparar la nueva versión antes de sustituirla, conservar licencias y actualizar el registro.
