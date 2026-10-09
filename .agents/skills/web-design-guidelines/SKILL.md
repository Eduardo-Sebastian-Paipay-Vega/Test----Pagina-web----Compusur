---
name: web-design-guidelines
description: Revisar UX, accesibilidad y presentación de las fuentes o vista previa de COMPUSUR, considerando las limitaciones del tema y la integración con Odoo. Usar en auditorías o revisiones de interfaces de este proyecto.
metadata:
  author: vercel
  version: "1.0.0-compusur"
---

# Web Design Guidelines para COMPUSUR

Adaptación local de la habilidad de Vercel. Conserva [la habilidad original](references/upstream-SKILL.md) y [una copia de las directrices](references/web-interface-guidelines.md). Las versiones y procedencia constan en `.agents/skills/sources.lock.json`, desde la raíz del proyecto.

Lee [las reglas de integración](../compusur-odoo-design/SKILL.md). Cuando la solicitud identifica una pantalla o archivos, usa ese alcance; no preguntes de nuevo qué revisar. Para una revisión general de esta biblioteca, empieza en `src/` y la vista previa generada.

## Revisión

1. Consulta las directrices oficiales actuales en `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` mediante una herramienta de lectura disponible. Si no hay acceso, usa la copia local y señala su fecha/versionado; no desactives la verificación TLS para obtenerla.
2. Aplica solo las reglas relevantes al stack y a los elementos revisados. Ejemplos de React/Next.js no son requisitos para QWeb o HTML estático.
3. Comprueba etiquetas y semántica, teclado/foco, contraste, texto largo, controles táctiles, tablas e imágenes adaptables, reducción de movimiento y mensajes útiles. No ocultar errores con `overflow:hidden` cuando recorta contenido esencial.
4. Distingue problemas del prototipo de funciones reales de Odoo. Precio, stock, pago, entrega y recepción de formularios no se validan con marcadores estáticos ni con HTTP 200.
5. Presenta hallazgos concretos con archivo y línea, efecto para el cliente y corrección. Usa enlaces locales clicables. Prioriza problemas demostrados; no producir una lista de advertencias hipotéticas.

Si el usuario pide correcciones, realiza las locales dentro del alcance solicitado y comprueba el resultado. Revisar una web pública no autoriza modificarla. No subir fuentes, claves ni datos privados a servicios externos de auditoría.
