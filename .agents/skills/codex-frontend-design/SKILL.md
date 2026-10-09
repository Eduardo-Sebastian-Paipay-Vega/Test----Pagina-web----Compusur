---
name: codex-frontend-design
description: Aplicar la variante de Frontend Design para Codex cuando se elija esta alternativa para diseñar o revisar visualmente COMPUSUR. Mantener HTML y CSS compatibles con la integración a Odoo.
license: Apache-2.0
---

# Codex Frontend Design para COMPUSUR

Adaptación del repositorio de dobromirdikov, basado en Frontend Design de Anthropic. Conserva [el original](references/upstream-SKILL.md) y la licencia Apache-2.0 en `LICENSE`. Lee el original para su composición y revisión visual cuando se elija esta alternativa.

Lee primero [las reglas de COMPUSUR](../compusur-odoo-design/SKILL.md). Esta variante es una alternativa a `frontend-design`, no una segunda etapa obligatoria del mismo diseño.

- Ajusta la composición al comercio de computadoras: categoría o producto claros, búsqueda reconocible, acceso directo a ficha y cotización. No convertir la tienda en una landing genérica de SaaS ni producir un dashboard sin relación con la solicitud.
- Trabaja con las fuentes existentes en `src/`, CSS limitado a `.cs-site` y el generador Python. Las sugerencias del original para frameworks, librerías de animación o aplicaciones completas solo aplican a un trabajo independiente que realmente los use; no cambian el stack de Odoo.
- Utiliza recursos de marca y producto autorizados. El generador de imágenes puede apoyar banners conceptuales si la solicitud lo requiere, pero no falsificar el aspecto ni las características de un producto vendido.
- Una preferencia estética del original no obliga a eliminar componentes útiles, sustituir fuentes que funcionan o rehacer toda la página. Atiende al diseño acordado y al alcance concreto del usuario.
- Revisa alrededor de 1440 px, 768 px y 390 px en cambios sustanciales; comprueba consola, foco, navegación y ausencia de cortes. No declarar funcionalidades comerciales listas para producción basándose solo en una vista previa.

Consulta `docs/ODOO.md` desde la raíz al preparar la integración. Exporta con `python scripts/project.py check`. Precios, inventario, carrito y formularios deben conectarse al sistema real al implementar una solicitud autorizada.
