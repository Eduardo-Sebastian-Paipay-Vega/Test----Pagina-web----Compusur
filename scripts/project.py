"""Vista previa y exportación local. Solo biblioteca estándar de Python."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from export_policy import ASSET_EXTENSIONS, validate_asset, validate_export
import argparse
import hashlib
import json
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'

def read(path):
    return (SRC / path).read_text(encoding='utf-8')

def products():
    rows = json.loads(read('data/products.sample.json'))
    for row in rows:
        if not row['url'].startswith('/shop') or '\\' in row['url'] or '://' in row['url']:
            raise ValueError('Destino de producto fuera del catálogo previsto')
    return rows

def product_markup(export=False):
    parts = []
    for row in products():
        label = 'Ver ficha y precio' if row['verified_product_url'] else 'Consultar catálogo'
        if export:
            action = f'<a class="cs-product-link" href="{escape(row["url"], quote=True)}">{label} →</a>'
        else:
            action = f'<button type="button" data-details="{escape(row["name"], quote=True)}" data-url="{escape(row["url"], quote=True)}">{label} →</button>'
        parts.append(f'''<article class="cs-product" data-product data-category="{escape(row['category'], quote=True)}">
  <div class="cs-drawing"><small>Imagen del producto pendiente</small></div>
  <div class="cs-eyebrow">{escape(row['category'])}</div>
  <h3>{escape(row['name'])}</h3><p>{escape(row['specs'])}</p>
  {action}
</article>''')
    return '\n'.join(parts)

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def styles():
    return read('styles/tokens.css') + '\n' + read('styles/site.css') + '''
.cs-site .cs-product-link{margin-top:auto;border-top:1px solid var(--cs-line);color:var(--cs-blue);font-size:12px;display:block;padding:12px 0;text-decoration:none}
.cs-site .cs-actions>a,.cs-site .cs-quote>a{display:inline-flex;align-items:center;min-height:44px;text-decoration:none}
.cs-site .cs-paths>a{display:flex;align-items:center;padding:15px;background:var(--cs-soft);border-radius:8px;gap:13px;color:var(--cs-ink);text-decoration:none}
'''

def source_assets():
    assets = []
    asset_root = SRC / 'assets'
    if asset_root.is_symlink():
        raise ValueError('La carpeta de recursos no puede ser un enlace externo')
    for source in (SRC / 'assets').rglob('*'):
        if not source.is_file() or source.name == 'README.md':
            continue
        if source.suffix.lower() not in ASSET_EXTENSIONS:
            raise ValueError(f'Recurso no permitido en el paquete: {source.name}')
        if source.is_symlink():
            raise ValueError('No se empaquetan recursos enlazados fuera del proyecto')
        source.resolve().relative_to(asset_root.resolve())
        assets.append((source.relative_to(asset_root), source))
    return assets

def copy_assets(destination, assets=None):
    copied = []
    for relative, source in source_assets() if assets is None else assets:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        copied.append(target)
    return copied

def build():
    target = ROOT / 'preview'
    home = read('blocks/inicio.html').replace('{{PRODUCTS}}', product_markup())
    document = read('pages/index.html').replace('{{HEADER}}',read('partials/header.html')).replace('{{HOME}}',home).replace('{{FOOTER}}',read('partials/footer.html'))
    if re.search(r'\{\{[A-Z_]+\}\}',document):
        raise ValueError('Quedaron marcadores sin resolver')
    write(target / 'index.html', document)
    write(target / 'assets/tokens.css', read('styles/tokens.css'))
    write(target / 'assets/site.css', styles().split(read('styles/tokens.css'),1)[1])
    write(target / 'assets/preview.js', read('scripts/preview.js'))
    copy_assets(target / 'assets/media')
    print(f'Vista previa: {target / "index.html"}')
    return target

def prepare_export():
    home = read('blocks/inicio.html').replace('{{PRODUCTS}}', product_markup(export=True))
    category_urls={'Todos':'/shop','Laptops':'/shop/category/laptops-9','Computadoras':'/shop/category/computadoras-10','Monitores':'/shop/category/monitor-17'}
    def replace_button(match):
        attrs, body = match.group(1), match.group(2)
        selection = re.search(r'data-filter="([^"]+)"',attrs)
        action = re.search(r'data-action="([^"]+)"',attrs)
        if not selection and not action:
            raise ValueError('Botón sin destino exportable')
        url = category_urls[selection.group(1)] if selection else '/contactus'
        cls = re.search(r'class="([^"]+)"',attrs)
        class_attr = f' class="{cls.group(1)}"' if cls else ''
        return f'<a{class_attr} href="{url}">{body}</a>'
    home = re.sub(r'<button\b([^>]*)>(.*?)</button>',replace_button,home,flags=re.S)
    fragment = '<!-- BORRADOR DE DISEÑO: revisar contenido y recursos antes de publicar. -->\n<section class="cs-site" aria-label="Inicio COMPUSUR propuesto">\n'+home+'\n</section>\n'
    css = styles()
    assets = source_assets()
    return fragment, css, assets

def export_odoo():
    fragment, css, assets = prepare_export()
    # Obligatorio para export y check: no escribir ni reemplazar el ZIP si falla.
    validate_export(fragment, css, assets)
    target = ROOT / 'dist/odoo'
    write(target / 'inicio.fragment.html', fragment)
    write(target / 'compusur.css', css)
    current_assets = copy_assets(target / 'assets/media', assets)
    manifest = {'status':'draft','validation':'local-static-contract-v1','odoo_compatibility':'pending-in-odoo-review','target':'COMPUSUR website_id=1','format':'HTML fragment + scoped CSS; not an installable Odoo module','contains_live_connection':False,'unresolved':['Logotipo original','Imágenes reales de productos','Vinculación dinámica a precios/stock','Verificación de características y enlaces de productos','Destino real de cotizaciones'],'files':{}}
    package_files = [target/'inicio.fragment.html',target/'compusur.css'] + current_assets
    for path in package_files:
        manifest['files'][path.relative_to(target).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    write(target / 'manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    zip_path=ROOT/'dist/compusur-diseno-borrador.zip'
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
        for path in package_files + [target/'manifest.json']:
            archive.write(path,path.relative_to(target).as_posix())
    print(f'Borrador para adaptar a Odoo: {zip_path}')
    return target

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors=[]
        self.ids=set()
    def handle_starttag(self,tag,attrs):
        attributes=dict(attrs)
        if 'id' in attributes:
            if attributes['id'] in self.ids:self.errors.append('ID duplicado: '+attributes['id'])
            self.ids.add(attributes['id'])
        if tag=='img' and 'alt' not in attributes:self.errors.append('Imagen sin texto alternativo')
        if tag in {'script','iframe','form'}:self.errors.append('Elemento activo en exportación: '+tag)
        for key,value in attrs:
            if key.startswith('on'):self.errors.append('Evento incrustado en exportación')
            if key in {'href','src'} and value and value.startswith(('javascript:','data:','http:','https:')):self.errors.append('Destino externo o activo sin revisar: '+value)

def check():
    build()
    target=export_odoo()
    fragment=(target/'inicio.fragment.html').read_text(encoding='utf-8')
    inspector=Inspector();inspector.feed(fragment)
    if '{{' in fragment:inspector.errors.append('Marcador sin resolver')
    if 'data-filter=' in fragment or 'data-action=' in fragment:inspector.errors.append('Control local en exportación')
    if inspector.errors:raise ValueError('; '.join(inspector.errors))
    manifest=json.loads((target/'manifest.json').read_text(encoding='utf-8'))
    for name,digest in manifest['files'].items():
        if hashlib.sha256((target/name).read_bytes()).hexdigest()!=digest:raise ValueError('Huella distinta: '+name)
    print('Validado: fragmento sin scripts/formularios, destinos locales, IDs únicos y paquete con huellas correctas.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','preview','export','check'])
    parser.add_argument('--port',type=int,default=8767)
    args=parser.parse_args()
    if args.command=='build':build()
    elif args.command=='export':export_odoo()
    elif args.command=='check':check()
    else:
        target=build()
        server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(SimpleHTTPRequestHandler,directory=str(target)))
        print(f'Vista previa local: http://127.0.0.1:{args.port}/',flush=True)
        try:server.serve_forever()
        except KeyboardInterrupt:pass
        finally:server.server_close()

if __name__=='__main__':main()
