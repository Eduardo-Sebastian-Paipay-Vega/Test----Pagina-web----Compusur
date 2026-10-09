---
name: react-best-practices
description: Aplicar las reglas de rendimiento de Vercel únicamente al escribir, revisar o modificar código React o Next.js que ya exista en el alcance solicitado. No usar para HTML, CSS o QWeb de COMPUSUR ni para introducir un framework en Odoo.
license: MIT
metadata:
  author: vercel
  version: "1.0.0-compusur"
---

# React Best Practices — uso condicionado

La biblioteca COMPUSUR actual usa HTML, CSS, JavaScript local y Python; no contiene React ni Next.js. Esta habilidad está instalada para una futura tarea que sí use esas tecnologías. No inicia una migración ni justifica agregar Node.js, npm, React, Next.js, Tailwind, un servidor SSR o dependencias al proyecto actual.

Lee [las limitaciones de integración](../compusur-odoo-design/SKILL.md). Si la tarea no contiene React o Next.js, no cargues las 70 reglas ni el documento compilado: usa la habilidad de diseño o revisión de interfaces que corresponda.

Cuando sí haya código React/Next.js en el alcance autorizado, consulta [la entrada original](references/upstream-SKILL.md) para priorizar reglas. Lee únicamente los archivos pertinentes de `rules/`; [AGENTS.md](AGENTS.md) contiene el documento compilado completo. Confirma la versión y arquitectura del proyecto antes de aplicar APIs específicas de una versión.

Se puede trasladar un principio general de JavaScript, como evitar trabajo repetido demostrado, a `src/scripts/preview.js` cuando resuelva un problema real. No convertir ejemplos de hooks, Server Components, SWR o `next/dynamic` en requisitos de Odoo.

Un experimento independiente con React requiere su propio alcance y una decisión sobre cómo se integraría. No incluir JSX, bundles de React o módulos de servidor en `dist/odoo` por defecto. Las funciones comerciales siguen perteneciendo a Odoo.
