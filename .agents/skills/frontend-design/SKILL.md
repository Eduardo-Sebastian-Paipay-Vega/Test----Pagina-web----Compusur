---
name: frontend-design
description: Diseñar y mejorar las páginas y bloques de COMPUSUR en HTML y CSS, con identidad visual propia y adaptación a Odoo. Usar como habilidad principal de diseño en compusur-web.
license: Complete terms in LICENSE.txt
---

# Frontend Design para COMPUSUR

Adaptación local de la habilidad de Anthropic. El texto original está en [references/upstream-SKILL.md](references/upstream-SKILL.md); consúltalo al definir dirección visual, tipografía, composición o redacción. Su contexto ficticio sobre un cliente que rechazó diseños no describe a COMPUSUR.

Lee primero [las reglas de integración del proyecto](../compusur-odoo-design/SKILL.md). La marca, el catálogo y el propósito comercial ya están identificados: encontrar equipos, comprar o pedir una cotización. Usa el contexto disponible para tomar decisiones; no hagas preguntas redundantes.

## Aplicación a esta biblioteca

- Define una dirección visual breve antes de un rediseño sustancial. Conserva el logotipo original y el azul de marca salvo que el usuario pida cambiarlos. El diseño propuesto sirve como base de conversación, no como una restricción estética inamovible.
- Implementa en `src/blocks/`, `src/partials/` y `src/styles/`; limita CSS a `.cs-site`. El formato de salida es HTML y CSS adaptables a los bloques y vistas de Odoo. No introducir React, Next.js, Tailwind, servidores nuevos o un sistema de compra paralelo para mejorar el aspecto.
- Evalúa legibilidad, contraste, navegación y jerarquía. Usa fuentes disponibles o recursos autorizados; una elección tipográfica no obliga a descargar una biblioteca ni cargar un CDN. Añade movimiento solo cuando aporte información, con respeto a `prefers-reduced-motion`.
- El contenido provisional debe indicarse como tal. No generar reseñas, cifras comerciales, precios, descuentos, stock o condiciones para llenar secciones. Las imágenes de un producto deben corresponder a ese producto; una ilustración conceptual no sustituye una fotografía comercial.
- Revisa cambios sustanciales en navegador en escritorio, tablet y móvil. Comprueba foco, texto largo, imágenes y desbordamiento. Ejecuta `python scripts/project.py check` si cambia el contenido exportable.

Usa esta habilidad o `codex-frontend-design` como dirección de diseño de una tarea, según lo solicitado; no acumules dos procesos completos que cubren lo mismo. Combínala con `web-design-guidelines` para una revisión cuando corresponda. Instalar la habilidad no publica el resultado en Odoo.
