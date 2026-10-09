"""Diagnóstico local sin publicar, conectar a Odoo ni regenerar el paquete."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse
import hashlib
import json
import re

import project
from export_policy import validate_export

ROOT = Path(__file__).resolve().parents[1]

def audit():
    errors = []
    fragment = None
    try:
        fragment, css, assets = project.prepare_export()
        validate_export(fragment, css, assets)
    except (ValueError, KeyError, OSError, TypeError, json.JSONDecodeError) as error:
        errors.append(str(error))
    files = sorted(path for path in (ROOT / 'src').rglob('*') if path.is_file())
    fingerprints = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    try:
        rows = project.products()
    except (ValueError, KeyError, OSError, TypeError, json.JSONDecodeError):
        rows = []
    pending = [
        'Probar inserción, recursos, permisos y herencias del tema dentro de Odoo, sitio COMPUSUR 1.',
        'Conectar precios, imágenes, stock, búsqueda y carrito a funciones nativas; las muestras son estáticas.',
        'Verificar destino y recepción real de cotizaciones; el prototipo no envía consultas.',
        'Confirmar datos comerciales pendientes antes de publicarlos.',
        'Revisar el resultado en escritorio, tablet y móvil; no se ejecutó revisión visual en este comando.',
        'Medir carga real y comportamiento de recursos dentro de Odoo; el tamaño local no demuestra velocidad.',
    ]
    if fragment and 'Imagen del producto pendiente' in fragment:
        pending.insert(0, 'Completar imágenes reales: el inicio exportable todavía contiene marcadores de imagen.')
    if rows:
        pending.insert(0, 'Verificar características y destinos actuales de los productos de muestra; las verificaciones guardadas no son comprobaciones de esta ejecución.')
    excluded = [path.relative_to(ROOT).as_posix() for path in files if path.suffix.lower() in {'.jsx','.tsx','.vue','.svelte','.py','.js'}]
    return {
        'checked_at': datetime.now(timezone(timedelta(hours=-5))).isoformat(timespec='seconds'),
        'local_status': 'BLOCKED' if errors else 'DRAFT_CONTRACT_PASSED',
        'odoo_status': 'NOT_VERIFIED_IN_ODOO',
        'publish_ready': False,
        'scope': 'Fuentes locales actuales de compusur-web; no consulta la web publicada ni el backend.',
        'errors': errors,
        'pending': pending,
        'excluded_runtime_sources': excluded,
        'sample_products': [{'name':row['name'], 'url':row['url'], 'previously_verified_product_url':row['verified_product_url']} for row in rows],
        'source_sha256': fingerprints,
    }

def markdown(result):
    lines = ['# Revisión local de compatibilidad con Odoo', '',
             'Fecha y hora de Lima: ' + result['checked_at'], '',
             '**Contrato local:** ' + result['local_status'], '',
             '**Validación dentro de Odoo:** pendiente. **Listo para publicar:** no.', '',
             result['scope'], '',
             'Este diagnóstico evalúa el contrato del borrador. Un bloqueo no significa que Odoo prohíba esa tecnología en todas las instalaciones.', '',
             '## Bloqueos detectados', '']
    lines.extend(['- ' + error.replace('\n',' ') for error in result['errors']] or ['No se detectaron bloqueos del contrato estático.'])
    lines += ['', '## Pendientes para una integración real', '']
    lines.extend('- ' + item for item in result['pending'])
    lines += ['', '## Código fuera de esta exportación', '']
    lines.extend('- `' + path + '`' for path in result['excluded_runtime_sources'])
    if not result['excluded_runtime_sources']:
        lines.append('No se encontraron fuentes de ejecución adicionales en src/.')
    lines += ['', '## Productos de muestra', '']
    for item in result['sample_products']:
        lines.append('- ' + item['name'] + ': `' + item['url'] + '`; requiere comprobación actual en Odoo.')
    lines += ['', '## Fuentes revisadas', '', 'Las huellas de la ejecución están en el informe JSON junto a este archivo.']
    lines.extend('- `' + name + '`' for name in result['source_sha256'])
    return '\n'.join(lines) + '\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', action='store_true', help='Guardar informe actual en docs/revisiones; no modificar src ni dist')
    args = parser.parse_args()
    result = audit()
    if args.report:
        folder = ROOT / 'docs/revisiones'
        folder.mkdir(parents=True, exist_ok=True)
        (folder/'odoo-compatibilidad-actual.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        (folder/'odoo-compatibilidad-actual.md').write_text(markdown(result), encoding='utf-8')
        print('Informe: ' + str(folder/'odoo-compatibilidad-actual.md'))
    print('Contrato local: ' + result['local_status'])
    print('Compatibilidad real en Odoo: pendiente; publicación no certificada.')
    for error in result['errors']:
        print('Bloqueo: ' + error)
    raise SystemExit(1 if result['errors'] else 0)

if __name__ == '__main__':
    main()
