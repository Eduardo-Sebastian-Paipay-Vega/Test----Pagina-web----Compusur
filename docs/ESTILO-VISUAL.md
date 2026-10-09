# Estilo visual COMPUSUR · versión 1

Establecido para el trabajo local el 9 de octubre de 2026, a petición del usuario de definir un estilo común. Dirección: **Tienda editorial tecnológica**. Usar esta referencia en las páginas nuevas y en mejoras del diseño; una solicitud posterior del usuario puede modificarla. No implica publicación ni aprobación de cada pantalla.

## Identidad

Una tienda de equipos con presentación clara, títulos expresivos y catálogo fácil de consultar. El protagonismo se reparte entre un mensaje principal en inicio y los productos reales en las pantallas comerciales. La composición debe ayudar a encontrar un equipo, comparar y comprar o pedir cotización.

Conservar `src/assets/COMPUSUR.png`, ya usado por la cabecera local, con sus proporciones originales. No redibujar, recolorear, recortar ni añadir efectos al logotipo. Presentarlo sobre una superficie que permita leerlo; revisar su legibilidad a tamaño móvil. Los tonos de interfaz siguientes son los actuales del proyecto, no una certificación de los colores corporativos originales.

## Paleta de interfaz

| Función | Valor | Token actual | Uso |
|---|---|---|---|
| Azul principal | `#1359CE` | `--cs-blue` | Acción principal, enlaces y banner de inicio |
| Blanco | `#FFFFFF` | `--cs-paper` | Fondo y superficies de lectura |
| Azul oscuro | `#142C49` | `--cs-ink` | Texto principal y superficies oscuras puntuales |
| Texto secundario | `#53657B` | `--cs-muted` | Descripciones y ayudas sobre fondo claro |
| Fondo suave | `#F0F5FB` | `--cs-soft` | Áreas de imagen y agrupaciones secundarias |
| Separadores | `#DCE5F0` | `--cs-line` | Bordes y divisiones discretas |
| Celeste de apoyo | `#C9E8FF` | `--cs-sky` | Ilustración o detalle decorativo puntual |

El azul principal identifica acciones; el celeste de apoyo no se usa como texto pequeño sobre blanco. Mantener foco de teclado visible con el tratamiento actual del CSS y comprobar contraste en cada combinación efectiva. Los colores de errores y estados comerciales se definen al integrar esos componentes, con texto e icono además del color.

## Tipografía

Familia de interfaz: `"Segoe UI", Arial, sans-serif`, ya configurada en `tokens.css`; sin una descarga de fuentes adicional. El resultado puede variar según las fuentes disponibles en el dispositivo.

- Texto general: 16 px, interlineado 1,6, párrafos de hasta 65 caracteres de ancho aproximado.
- Descripciones de producto y controles: 14–16 px; no reducir textos comerciales esenciales al tamaño de una nota.
- Título del inicio: escala actual de 42–76 px en escritorio y 39–61 px en móvil, con el ajuste existente del CSS. Revisar títulos largos para evitar cortes.
- Encabezados de sección: 26–38 px; títulos de producto: 20 px. Peso medio o fuerte para distinguir jerarquía.
- Una jerarquía principal por pantalla. En catálogo y ficha, usar títulos más contenidos que el banner de inicio para dar espacio a los equipos y sus acciones.

La tipografía del logotipo pertenece a la imagen; no se convierte en la fuente del resto del sitio.

## Composición y componentes

Mantener alineación predominantemente a la izquierda, ancho máximo actual de 1600 px y márgenes laterales cercanos al 5 %. Los espacios se organizan preferentemente en múltiplos de 4 u 8 px, ajustándolos cuando lo requiera el contenido.

| Componente | Regla visual |
|---|---|
| Cabecera | Logotipo, búsqueda y carrito con jerarquía clara; mismos destinos en todo el sitio |
| Navegación | Categorías legibles y acceso a cotización; estado activo visible |
| Banner de inicio | Un mensaje principal, una imagen pertinente, una acción dominante y otra secundaria |
| Acción principal | Azul con texto blanco; en el banner azul, blanco con texto azul; alto de referencia 48 px y radio 8 px |
| Acción secundaria | Menor énfasis; borde o enlace según el fondo, con contraste comprobado; no copiar texto blanco del banner sobre fondo blanco |
| Producto | Imagen proporcional, nombre, atributos útiles y acción; precio y stock reales al integrar; radio de imagen 12 px y separadores discretos |
| Bloque de cotización | Fondo claro y llamada concreta; radio de referencia 16 px |
| Contenedor de banner | Radio de referencia 24 px en escritorio y 18 px en móvil |
| Pie | Contacto y condiciones confirmadas, con jerarquía menor que el contenido comercial |

Evitar sombras en todas las tarjetas, adornos repetidos y carruseles automáticos. Usar bordes y espacio para organizar. Interacciones con área táctil de al menos 44 px como regla del proyecto. No convertir toda la página en tarjetas idénticas.

## Imágenes, iconos y movimiento

Fotos de productos: fondo limpio, objeto completo y tamaño visual comparable; usar `object-fit: contain` cuando corresponda. Las imágenes deben representar el modelo ofrecido. El inicio usa ahora `src/assets/banners/hero-equipos-ambiente.png` como imagen ambiental del borrador; no representa un SKU. Las tarjetas siguen pendientes de fotografías oficiales verificadas.

Guardar recursos autorizados en `src/assets/`, conservar proporciones, especificar dimensiones y texto alternativo según su función. La carga en Odoo y acceso público se verifican por separado. No poner el único título, precio o acción dentro de una imagen.

Usar un conjunto de iconos coherente que permita el entorno de Odoo, con etiquetas accesibles en acciones sin texto. Los símbolos de la vista previa son provisionales; no certifican el aspecto final de los iconos en producción. Añadir movimiento solo si explica un cambio y respetar reducción de movimiento.

## Adaptación por pantalla

- Inicio: banner editorial y accesos rápidos al catálogo; el mensaje principal no debe ocultar categorías o productos tras secciones innecesarias.
- Catálogo: dar prioridad a productos, búsqueda y filtros nativos. Mantener identidad compartida sin repetir el gran banner.
- Ficha: imagen, nombre, resumen, precio y compra próximos; características legibles en móvil.
- Contacto/cotización: título breve, campos necesarios y explicación del siguiente paso; destino de recepción pendiente de verificación real.
- Páginas informativas: ancho de lectura cómodo, títulos claros y acceso a contacto o catálogo según el propósito.

Mantener los puntos de adaptación actuales de 900 y 620 px como base local, no como garantía para todas las pantallas. Revisar cambios sustanciales a 1440, 768 y 390 px. En móvil, apilar contenido cuando sea necesario sin perder acciones ni esconder información esencial.

## Uso y cambios

`src/styles/tokens.css` contiene los valores actuales; `site.css` implementa los componentes. Este documento fija la dirección y describe tanto reglas existentes como criterios para próximas pantallas. No afirma que todos los componentes futuros estén implementados.

Cada nueva página debe seguir esta identidad y [el diseño integral](DISENO-INTEGRAL.md). Si una nueva necesidad requiere una excepción, documentar el motivo y actualizar la referencia junto con los estilos afectados. Evitar inventar una paleta, tipografía o botones diferentes por página.

El diseño se adapta a HTML/CSS y funciones nativas de Odoo según [el contrato de compatibilidad](COMPATIBILIDAD-ODOO.md). La validación dentro del tema real continúa siendo un paso de implementación.
