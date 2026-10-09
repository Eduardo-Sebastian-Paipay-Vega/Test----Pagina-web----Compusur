---
name: diseno-integral-odoo
description: Definir y mantener el diseño integral de COMPUSUR, decidir qué páginas necesita y coordinar las skills locales de diseño, UX y compatibilidad Odoo. Usar para arquitectura del sitio, nuevas páginas o coherencia entre pantallas.
---

# Diseño integral de COMPUSUR

Mantener una propuesta coherente desde inicio hasta compra o cotización. Coordinar las habilidades locales según el trabajo solicitado; orquestar no implica abrir subagentes ni publicar.

## Fuente de decisiones

Lee [las reglas de integración](../compusur-odoo-design/SKILL.md), [el diseño integral](../../../docs/DISENO-INTEGRAL.md) y, al decidir páginas, [las verificaciones de páginas](../../../docs/PAGINAS-ODOO.md). Si el trabajo trata de URLs inexistentes o enlaces rotos, sigue [el protocolo 404](../../../docs/PROTOCOLO-ENLACE-INEXISTENTE.md). Consulta [contenido pendiente](../../../docs/CONTENIDO.md) si el alcance afecta datos comerciales.

El documento integral es la referencia mantenida del proyecto. Separar decisiones del usuario, recomendaciones y asuntos pendientes; no presentar un plan propuesto como aprobación de todas sus páginas. Si hay conflicto entre documentos, aplicar la instrucción vigente del usuario y corregir la referencia afectada. Conservar la procedencia de decisiones importantes.

## Decidir qué página hace falta

Relacionar cada propuesta con una necesidad del cliente, contenido disponible y acción concreta. Comparar con páginas y funciones actuales antes de crear otra. Para cada página, registrar objetivo, ruta propuesta o existente, contenido, acción, destino nativo, prioridad y estado. Si falta contenido comercial, se puede diseñar el esqueleto indicando el pendiente.

No convertir categorías, fichas, carrito o checkout en páginas estáticas paralelas al comercio de Odoo. No consolidar páginas parecidas ni cambiar rutas de respuesta de formularios sin revisar sus usos. La captura de páginas aportada es evidencia parcial, no un inventario actual de permisos o publicación.

## Coordinar las skills

- Planificación: esta skill mantiene mapa del sitio, recorrido del cliente, componentes compartidos y pendientes en `docs/DISENO-INTEGRAL.md`.
- Diseño: usar [frontend-design](../frontend-design/SKILL.md) habitualmente; [codex-frontend-design](../codex-frontend-design/SKILL.md) si se solicita esa alternativa. Leer solo la dirección elegida y sus referencias pertinentes.
- Revisión de UX y accesibilidad: usar [web-design-guidelines](../web-design-guidelines/SKILL.md) al revisar pantallas o cambios sustanciales; esa skill describe su consulta de directrices actuales.
- Preparación para integrar o diagnóstico de compatibilidad: usar [verificar-odoo](../verificar-odoo/SKILL.md), con sus pruebas e informe. Un cambio exclusivamente documental no requiere generar una auditoría visual ficticia.
- Imágenes: consultar [la integración de recursos](../../../docs/IMAGENES-ODOO.md) cuando el trabajo incluya cargas reales. React Best Practices solo aplica si existe React en el alcance solicitado.

Mantener identidad, navegación, espaciado, tipografía, botones, tarjetas y estados coherentes con el documento integral y `src/styles/tokens.css`. Documentar cambios deliberados en lugar de imponer el mismo formato a todas las páginas. “Tienda editorial” es la referencia visual seleccionada en la propuesta; no equivale a aprobación de publicación.

## Entrega y alcance

Según la solicitud, actualizar el plan, implementar fuentes locales o preparar la integración concreta. Al entregar un plan, indicar la siguiente pantalla y los datos que faltan. Al cambiar diseño exportable, ejecutar las comprobaciones del proyecto y revisar las pantallas afectadas. No declarar que otras páginas se exportan si el generador aún solo selecciona inicio.

No modificar permisos, activar escritura genérica, crear páginas en producción o publicar por invocar esta skill. Si se solicita implementación real, verificar las herramientas y capacidades actuales, respaldos y destinos de integración según las reglas del proyecto, y actuar dentro de esa solicitud.
