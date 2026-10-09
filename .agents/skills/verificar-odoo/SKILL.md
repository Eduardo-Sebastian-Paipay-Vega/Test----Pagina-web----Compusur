---
name: verificar-odoo
description: Auditar la página actual de COMPUSUR y su exportación para determinar qué puede adaptarse a Odoo, qué incumple el contrato local y qué requiere prueba real. Usar cuando se pida verificar compatibilidad, límites o preparación para importar a Odoo; no publica ni modifica la tienda.
---

# Verificar la página para Odoo

Emitir un diagnóstico basado en el contenido actual y en evidencias. Distinguir preparación de diseño, compatibilidad del entorno y funcionamiento comercial; no convertir una comprobación local exitosa en una garantía de importación o publicación.

## Alcance al llamarla

Identifica la raíz por `compusur-web.code-workspace`. Lee [las reglas del proyecto](../compusur-odoo-design/SKILL.md), [el contrato de exportación](../../../docs/COMPATIBILIDAD-ODOO.md) y [la integración](../../../docs/ODOO.md).

Si el usuario no indica otra página, revisa las fuentes actuales de esta biblioteca y su vista previa completa: inicio, cabecera, pie, estilos, scripts, datos y recursos. Indica ese alcance al comenzar; no preguntar de nuevo por una página que ya está identificada en la sesión. Si señala una URL o página publicada, inspecciónala en lectura y compárala con el diseño local cuando estén disponibles ambos. No atribuir al sitio público funciones que solo existen en la propuesta.

Esta skill autoriza diagnóstico, comandos locales de lectura e informe. No cambia fuentes, permisos, clave API, estado de publicación, precios, productos ni vistas de Odoo por el hecho de invocarla. Si el usuario también pide corregir, atiende las correcciones autorizadas y repite las comprobaciones pertinentes.

## Diagnóstico local

1. Ejecuta `python scripts/audit_odoo.py --report` desde la raíz. Lee `docs/revisiones/odoo-compatibilidad-actual.md` y su JSON. El script inspecciona sin regenerar dist ni conectarse a Odoo; el informe identifica las fuentes por SHA-256. Si devuelve un bloqueo, analiza el motivo sin quitar la política de exportación.
2. Lee las fuentes de la página, incluyendo el JavaScript excluido del paquete. Comprueba qué características desaparecerían al exportar, qué es una simulación y qué necesitaría una función nativa de Odoo. Revisa el ZIP existente solo si corresponde: puede ser anterior a las fuentes actuales; no usarlo como evidencia del estado actual sin comparar sus huellas con una construcción vigente.
3. Para la revisión visual, usa la vista previa local y el navegador disponibles. Evalúa escritorio, tablet y móvil en cambios sustanciales: foco/teclado, controles, legibilidad, imágenes, tablas, texto largo y desbordamiento. Una apariencia correcta no prueba formularios, pagos ni inventario.
4. Revisa dependencias, rutas portables, referencias a recursos y tamaño de archivos. Evita frameworks o librerías innecesarios para el diseño. Distingue mediciones de rendimiento de simples estimaciones; no afirmar que es rápido por usar HTML o por tener archivos pequeños.

## Comprobar lo que realmente soporta el entorno

La referencia anterior es COMPUSUR en Odoo Online SaaS 19.3, sitio 1; no asumir que esa versión, sus permisos o su tema siguen iguales. Usa herramientas conectadas de lectura cuando estén disponibles para comprobar versión/tipo de despliegue, sitio, editor, plantillas efectivas, herencias y recursos relacionados. Si no hay acceso, registra qué datos proceden de la auditoría previa y qué sigue sin comprobar.

Para una capacidad técnica dudosa, un cambio de versión o una propuesta fuera del contrato, consulta documentación oficial de Odoo correspondiente al entorno y enlaza la evidencia. No usar restricciones de nuestro generador como si fueran prohibiciones universales de Odoo. Por ejemplo: un script, iframe o QWeb fuera del paquete actual puede requerir una adaptación específica; un proyecto Next.js o Python no se vuelve instalable en Odoo Online por subir su carpeta.

Mapea cada característica a un destino concreto: bloque de página, CSS de alcance limitado, adjunto, catálogo nativo, plantilla efectiva o integración específica. Si no puede identificarse ese destino, clasifica la característica como pendiente en lugar de declararla importable.

Comprueba, según el alcance, enlaces/productos, origen de precios y disponibilidad, carrito/checkout, destino de cotización y recursos. Usa datos comerciales confirmados; consulta [contenido pendiente](../../../docs/CONTENIDO.md). Las consultas en lectura no prueban compra, pago ni entrega de un formulario: indica esas pruebas como pendientes si no se realizaron por separado.

## Informe obligatorio

Amplía el informe generado con el análisis manual y la evidencia visual o de Odoo obtenida en esta ejecución. Conserva sus huellas y fecha, y distingue resultados automáticos de observaciones manuales. Añade una tabla con **elemento, destino de integración, estado, evidencia y corrección pendiente**.

Usa estados precisos:

- **Bloqueado por el contrato local:** explicar qué impide preparar el paquete y cómo adaptarlo.
- **Preparado como borrador:** pasa comprobaciones locales, pero todavía no tiene prueba de integración real.
- **Pendiente de verificación en Odoo:** requiere comprobar versión, permisos, plantillas, recursos o conexión funcional.
- **Verificado en Odoo:** solo para el elemento concreto probado en ese entorno; describir la prueba y sus límites.

La conclusión debe indicar: alcance revisado, bloqueos, funcionalidades de muestra, pendientes y siguiente acción concreta. No utilizar porcentajes de compatibilidad inventados, ni llamar a toda la web «lista para importar» porque un fragmento pasa las pruebas. En la respuesta final, enlaza el informe y resume los problemas que impiden una implementación real. Si todo pasa localmente, comunica los pendientes dentro de Odoo.
