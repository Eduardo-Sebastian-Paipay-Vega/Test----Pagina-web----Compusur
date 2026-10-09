"""Aplicar adaptaciones locales conservando los originales descargados."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents/skills'

ADAPTATIONS = {
    'frontend-design': '''---
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
''',
    'codex-frontend-design': '''---
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
''',
    'web-design-guidelines': '''---
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
''',
    'react-best-practices': '''---
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
'''
}

SOURCES = [
    {'skill':'frontend-design','repo':'anthropics/skills','commit':'9d630808e4add0a7146de4af9384155d5dee350a','path':'skills/frontend-design'},
    {'skill':'codex-frontend-design','repo':'dobromirdikov/codex-frontend-design-skill','commit':'983119775a936d123df9fbfbc3821bdee5bb58fd','path':'skills/frontend-design'},
    {'skill':'web-design-guidelines','repo':'vercel-labs/agent-skills','commit':'063bee94c3f4df8453406c830b0a7df0f2860278','path':'skills/web-design-guidelines'},
    {'skill':'react-best-practices','repo':'vercel-labs/agent-skills','commit':'063bee94c3f4df8453406c830b0a7df0f2860278','path':'skills/react-best-practices'},
]

def main():
    for entry in SOURCES:
        folder = SKILLS / entry['skill']
        references = folder / 'references'
        references.mkdir(exist_ok=True)
        original = references / 'upstream-SKILL.md'
        if not original.exists():
            shutil.copyfile(folder / 'SKILL.md', original)
        metadata = folder / 'agents/openai.yaml'
        if metadata.exists() and not (references / 'upstream-openai.yaml').exists():
            shutil.copyfile(metadata, references / 'upstream-openai.yaml')
        (folder / 'SKILL.md').write_text(ADAPTATIONS[entry['skill']],encoding='utf-8')
        entry['source_url'] = f"https://github.com/{entry['repo']}/tree/{entry['commit']}/{entry['path']}"
        entry['original_sha256'] = hashlib.sha256(original.read_bytes()).hexdigest()
        entry['adapted_sha256'] = hashlib.sha256((folder/'SKILL.md').read_bytes()).hexdigest()
    record={'configured_on':'2026-10-09','scope':'project only','sources':SOURCES,'guidelines_snapshot':{'repo':'vercel-labs/web-interface-guidelines','commit':'434b7f91364665f2f733b310ec54809bf8f37937','path':'command.md'}}
    (SKILLS / 'sources.lock.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Cuatro skills adaptadas; originales y versiones conservados.')

if __name__ == '__main__':
    main()
