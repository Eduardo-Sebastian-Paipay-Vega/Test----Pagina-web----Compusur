"""Validación local de skills sin dependencias o acceso a internet."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents/skills'

def main():
    names = set()
    errors = []
    for folder in sorted(SKILLS.iterdir()):
        if not folder.is_dir():
            continue
        entry = folder / 'SKILL.md'
        if not entry.is_file():
            errors.append(f'{folder.name}: falta SKILL.md')
            continue
        text = entry.read_text(encoding='utf-8')
        front = re.match(r'^---\n(.*?)\n---', text, re.S)
        if not front:
            errors.append(f'{folder.name}: encabezado no válido')
            continue
        name = re.search(r'^name: ([a-z0-9-]+)$', front.group(1), re.M)
        description = re.search(r'^description: (.+)$', front.group(1), re.M)
        if not name or not description:
            errors.append(f'{folder.name}: falta nombre o descripción')
            continue
        if name.group(1) != folder.name or name.group(1) in names:
            errors.append(f'{folder.name}: nombre distinto o duplicado')
        names.add(name.group(1))
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in target or target.startswith('#'):
                continue
            path = (folder / target.split('#')[0]).resolve()
            try:
                path.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f'{folder.name}: referencia fuera del proyecto')
                continue
            if not path.exists():
                errors.append(f'{folder.name}: referencia inexistente {target}')
        print(f'Revisada: {folder.name}')
    record = json.loads((SKILLS / 'sources.lock.json').read_text(encoding='utf-8'))
    for source in record['sources']:
        folder = SKILLS / source['skill']
        original = folder / 'references/upstream-SKILL.md'
        if not original.is_file() or hashlib.sha256(original.read_bytes()).hexdigest() != source['original_sha256']:
            errors.append(source['skill'] + ': original distinto del registrado')
        current = hashlib.sha256((folder / 'SKILL.md').read_bytes()).hexdigest()
        if current != source['adapted_sha256']:
            print('Cambio local desde la configuración inicial: ' + source['skill'])
    expected = {'compusur-odoo-design','frontend-design','codex-frontend-design','web-design-guidelines','react-best-practices','verificar-odoo','diseno-integral-odoo'}
    if names != expected:
        errors.append('La selección instalada no coincide con las siete skills previstas')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Skills verificadas: nombres únicos, referencias y originales correctos.')

if __name__ == '__main__':
    main()
