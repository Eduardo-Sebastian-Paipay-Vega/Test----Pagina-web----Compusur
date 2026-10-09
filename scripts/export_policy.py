"""Contrato del borrador estático de COMPUSUR; no certifica publicación en Odoo."""
from html.parser import HTMLParser
from pathlib import PurePosixPath
import re
import xml.etree.ElementTree as ET

ASSET_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.avif', '.svg', '.woff', '.woff2'}

def local_destination(value):
    value = value.strip()
    if not value or re.search(r'[\\\x00-\x20]', value):
        return False
    if value.startswith('#'):
        return True
    if value.startswith('//') or re.search(r'^[a-z][a-z0-9+.-]*:', value, re.I):
        return False
    if value.startswith('/'):
        return True
    return value.startswith('assets/media/') and '..' not in PurePosixPath(value).parts

class FragmentInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.ids = set()
        self.resources = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in {'script','iframe','form','input','select','textarea','button','style','link','object','embed','html','head','body','base','meta'}:
            self.errors.append('Elemento fuera del contrato de bloque estático: ' + tag)
        if tag == 'img' and 'alt' not in attributes:
            self.errors.append('Imagen sin texto alternativo')
        if 'id' in attributes:
            if attributes['id'] in self.ids:
                self.errors.append('ID duplicado: ' + attributes['id'])
            self.ids.add(attributes['id'])
        for key, value in attrs:
            if key.startswith('on') or key.startswith('t-') or key in {'data-filter','data-action','data-details'}:
                self.errors.append('Atributo de ejecución o demostración no exportable: ' + key)
            if key == 'style':
                self.errors.append('Mover el estilo incrustado a CSS limitado a .cs-site')
            values = [value] if key in {'href','src','poster','xlink:href'} else []
            if key == 'srcset' and value:
                values = [part.strip().split()[0] for part in value.split(',') if part.strip()]
            for destination in values:
                if destination and not local_destination(destination):
                    self.errors.append('Destino externo, activo o local no portable: ' + destination)
                elif destination and destination.startswith('assets/media/'):
                    self.resources.add(destination.split('?')[0].split('#')[0])

def css_resources(css):
    resources = set()
    for match in re.finditer(r'url\(\s*([^)]+)\)', css, re.I):
        value = match.group(1).strip().strip('\"\'')
        if not local_destination(value):
            raise ValueError('Recurso CSS externo o no portable: ' + value)
        if value.startswith('assets/media/'):
            resources.add(value.split('?')[0].split('#')[0])
    return resources

def validate_css(css):
    clean = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    if re.search(r'@import\b|expression\s*\(|javascript\s*:', clean, re.I):
        raise ValueError('CSS con importación o ejecución fuera del contrato')
    resources = css_resources(clean)
    # Recorre bloques respetando cadenas y paréntesis; solo admite contenedores
    # media/supports/container/layer y reglas que empiecen por .cs-site.
    def walk(text):
        start = 0
        while start < len(text):
            opening = text.find('{', start)
            if opening < 0:
                if text[start:].strip():
                    raise ValueError('Declaración CSS fuera de una regla revisable')
                return
            header = text[start:opening].strip()
            depth = 1; quote = None; index = opening + 1
            while index < len(text) and depth:
                char = text[index]
                if quote:
                    if char == '\\':
                        index += 2
                        continue
                    if char == quote:
                        quote = None
                elif char in '\"\'':
                    quote = char
                elif char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                index += 1
            if depth:
                raise ValueError('Bloque CSS sin cerrar')
            body = text[opening+1:index-1]
            if header.startswith('@'):
                if not re.match(r'^@(media|supports|container|layer)\b', header, re.I):
                    raise ValueError('Regla CSS global no revisada: ' + header)
                walk(body)
            else:
                for selector in header.split(','):
                    if not re.match(r'^\.cs-site(?=[\s.:#>+~\[]|$)', selector.strip()):
                        raise ValueError('Selector CSS fuera de .cs-site: ' + selector.strip())
            start = index
    walk(clean)
    return resources

def validate_asset(path):
    if path.suffix.lower() not in ASSET_EXTENSIONS:
        raise ValueError('Recurso fuera de la lista permitida: ' + path.name)
    if path.suffix.lower() == '.svg':
        tree = ET.fromstring(path.read_bytes())
        for element in tree.iter():
            tag = element.tag.split('}')[-1].lower()
            if tag in {'script','foreignobject','style'}:
                raise ValueError('SVG activo fuera del contrato: ' + path.name)
            for key, value in element.attrib.items():
                name = key.split('}')[-1].lower()
                if name.startswith('on') or (name in {'href','src'} and not value.startswith('#')):
                    raise ValueError('SVG con ejecución o recursos externos: ' + path.name)

def validate_export(fragment, css, assets):
    inspector = FragmentInspector()
    inspector.feed(fragment)
    inspector.close()
    if '{{' in fragment or '<%' in fragment:
        inspector.errors.append('Marcadores de plantilla sin resolver')
    if inspector.errors:
        raise ValueError('; '.join(inspector.errors))
    references = inspector.resources | validate_css(css)
    available = {'assets/media/' + relative.as_posix() for relative, _ in assets}
    missing = references - available
    if missing:
        raise ValueError('Recursos sin archivo en el paquete: ' + ', '.join(sorted(missing)))
    for _, path in assets:
        validate_asset(path)
