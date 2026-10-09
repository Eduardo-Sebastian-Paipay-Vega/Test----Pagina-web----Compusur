# Diseño integral de COMPUSUR

Referencia de trabajo del 9 de octubre de 2026. Estado: planificación local; no crea ni publica páginas.

## Dirección y objetivo

El objetivo es encontrar equipos y llegar a comprar o solicitar cotización con claridad. Referencia visual: “Tienda editorial”, seleccionada en la interacción de la propuesta. El alcance completo, contenidos y pantallas siguientes siguen siendo recomendaciones hasta que se trabajen según las indicaciones del usuario.

El estilo común queda establecido en [ESTILO-VISUAL.md](ESTILO-VISUAL.md), versión 1 del 9 de octubre de 2026, por la solicitud del usuario de definirlo para las siguientes páginas. Conservar el logotipo incorporado en `src/assets/COMPUSUR.png` y la paleta azul actual de interfaz. El inicio usa una imagen ambiental generada para el borrador; las fotografías definitivas de productos siguen pendientes. Los valores compartidos se editan en `src/styles/tokens.css`; los estilos quedan dentro de `.cs-site`. No convertir imágenes ambientales en fotografías de producto.

La auditoría UX/UI aportada el 9 de octubre de 2026 se aplicó al borrador: el hero ahora comunica equipos de tecnología, reduce el titular, usa acciones “Explorar catálogo” y “Solicitar cotización”, y añade el recorrido Explora–Compara–Continúa. Se mantuvieron pendientes los precios, stock, garantías, servicios empresariales, ubicación y marcas hasta contar con datos confirmados.

## Mapa propuesto y prioridades

| Pantalla | Destino | Propósito y acción | Decisión inicial |
|---|---|---|---|
| Inicio | `/` existente | Encontrar categorías y entrar al catálogo o cotización | Prioridad 1: mejorar la propuesta actual |
| Catálogo y categorías | Comercio nativo `/shop`; verificar rutas de categorías | Comparar y encontrar equipos reales | Prioridad 1: diseñar sobre funciones existentes |
| Ficha de producto | Rutas nativas de productos, verificadas por registro | Leer características, precio y comprar o consultar | Prioridad 1: corregir lectura móvil y proximidad de compra |
| Contacto/cotización | `/contactus` existente | Enviar una consulta con destino comprobado | Prioridad 1: diseñar; datos y recepción pendientes |
| Sobre nosotros | `/about-us` y `/acerca-de` visibles en captura | Presentar empresa y generar confianza | Prioridad 2: comparar antes de elegir o consolidar |
| Servicios | `/our-services` visible en captura | Explicar servicios reales y solicitar atención | Prioridad 2: conservar solo con oferta confirmada |
| Perú Compras | `/catalogo-peru-compras` visible en captura | Acceder a información y atención de ese canal | Pendiente: contenido y visibilidad comercial |
| Condiciones y privacidad | `/privacy` visible; otras rutas por decidir | Aclarar políticas reales | Revisar contenido confirmado; no inventar condiciones |
| Plan de precios | `/pricing` visible en captura | Por determinar según la oferta real | No priorizar sin una función comercial concreta |
| Agradecimientos y recepción | Rutas existentes de formularios/apps | Confirmar resultado del flujo correspondiente | Revisar vínculos; no añadir al menú comercial por defecto |

Esta tabla combina rutas de la captura, auditoría previa y propuestas. Verificar el inventario vivo antes de implementar. No implica que todas las páginas sean públicas ni que deban crearse nuevamente.

## Recorridos que debe sostener el diseño

- Compra: inicio → categoría/catálogo → ficha → carrito → checkout nativo.
- Cotización: inicio, catálogo o ficha → contacto/cotización → confirmación del envío y recepción comprobadas.
- Confianza: información de empresa, contacto y condiciones accesibles sin dificultar el acceso al catálogo.

## Componentes y consistencia

Mantener cabecera, navegación, búsqueda, carrito y pie coherentes con las capacidades reales del tema. Compartir tokens de color, tipografía y espaciado, estados de enlaces/botones, presentación de tarjetas y tratamiento de imágenes. Adaptar el contenido y jerarquía de cada pantalla a su propósito.

El inicio debe guiar al catálogo; la ficha debe acercar precio, disponibilidad y acción al resumen; el contacto debe explicar qué se solicita y qué ocurre al enviarlo. Catálogo, precios, stock y compra se obtienen de Odoo. Los controles actuales de la vista previa son demostraciones y no prueban estos recorridos.

Comprobar cambios sustanciales en escritorio, tablet y móvil, con teclado, foco, legibilidad y ausencia de desbordamiento. Medir rendimiento cuando exista un resultado real; no prometer rapidez por el estilo visual.

## Pendientes y alcance técnico

Pendientes comerciales conocidos: teléfono de ventas de Rocío, dirección, reglas de envío, pagos y visibilidad de Perú Compras. Diseñar áreas independientes sin inventar esos datos.

La vista previa local ya genera siete esqueletos navegables desde `src/data/pages.sample.json`, con navegación común y destinos de Odoo anotados. Se listan en [verificaciones de páginas](PAGINAS-ODOO.md). Estos enlaces no crean redirecciones. El generador de Odoo sigue exportando solo el bloque de inicio; agregar una pantalla local no la incorpora automáticamente al ZIP. El MCP general conserva lectura, y el MCP de imágenes solo carga adjuntos. La creación de páginas requiere comprobar capacidades y permisos disponibles al implementarla.

Aplicar [verificaciones de páginas](PAGINAS-ODOO.md), [contrato de exportación](COMPATIBILIDAD-ODOO.md) y [adaptación](ODOO.md). Una prueba local es un borrador, no una publicación validada en Odoo.

Para tratar enlaces rotos, seguir el [protocolo 404](PROTOCOLO-ENLACE-INEXISTENTE.md), que recoge la comprobación de la plantilla y las redirecciones de COMPUSUR.

## Mantenimiento y siguiente paso

Usar `$diseno-integral-odoo` para mantener esta referencia y coordinar las skills. Registrar nuevas decisiones aquí con fecha, motivo y origen; sustituir recomendaciones cuando el usuario las resuelva.

Siguiente paso recomendado: concretar el inicio con el enfoque seleccionado y sus componentes compartidos; después diseñar catálogo, ficha y contacto. No crear todas las páginas de la captura antes de revisar su utilidad y contenido.
