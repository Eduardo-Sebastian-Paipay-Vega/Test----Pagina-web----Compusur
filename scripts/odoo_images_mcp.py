"""MCP stdio limitado a crear imágenes del proyecto en COMPUSUR, sitio 1."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile

from export_policy import validate_asset

ROOT=Path(__file__).resolve().parents[1]
MAX_BYTES=5*1024*1024
TOOL={
    'name':'upload_website_image',
    'description':'Carga una imagen autorizada de src/assets a COMPUSUR sitio 1. Privada por defecto. public=true hace accesible el adjunto pero no modifica ni publica páginas. No edita productos, pedidos ni pagos. Hasta 5 MB. Devuelve URL y hash verificado.',
    'inputSchema':{'type':'object','properties':{'file':{'type':'string','description':'Ruta relativa a compusur-web; archivo en src/assets.'},'public':{'type':'boolean','default':False,'description':'Hacer accesible el recurso para uso web. Usar solo para recursos destinados a publicación.'}},'required':['file'],'additionalProperties':False},
    'annotations':{'readOnlyHint':False,'destructiveHint':False,'idempotentHint':False,'openWorldHint':True},
}

def image_path(value,public=False):
    path=Path(value)
    if not path.is_absolute():path=ROOT/path
    resolved=path.resolve(strict=True)
    asset_root=(ROOT/'src/assets').resolve()
    fixture_root=(ROOT/'tests/fixtures').resolve()
    is_fixture=resolved.is_relative_to(fixture_root)
    if not resolved.is_relative_to(asset_root) and not (is_fixture and not public):
        raise ValueError('Solo se permiten imágenes de src/assets; las pruebas deben ser privadas.')
    if path.is_symlink() or not resolved.is_file():raise ValueError('Archivo no permitido')
    if resolved.suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.svg'}:raise ValueError('Formato de imagen no permitido')
    data=resolved.read_bytes()
    if not 0<len(data)<=MAX_BYTES:raise ValueError('La imagen debe medir entre 1 byte y 5 MB')
    signatures={'.png':lambda b:b.startswith(b'\x89PNG\r\n\x1a\n'),'.jpg':lambda b:b.startswith(b'\xff\xd8\xff'),'.jpeg':lambda b:b.startswith(b'\xff\xd8\xff'),'.webp':lambda b:b[:4]==b'RIFF' and b[8:12]==b'WEBP'}
    if resolved.suffix.lower() in signatures and not signatures[resolved.suffix.lower()](data):raise ValueError('Contenido distinto de la extensión de imagen')
    validate_asset(resolved)
    return resolved

def upload(arguments):
    if set(arguments)-{'file','public'}:raise ValueError('Parámetros no permitidos')
    public=arguments.get('public',False)
    if not isinstance(public,bool):raise ValueError('public debe ser booleano')
    path=image_path(arguments['file'],public)
    relative=path.relative_to(ROOT).as_posix()
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    registry=ROOT/'odoo/media-registry.json'
    records=json.loads(registry.read_text(encoding='utf-8')) if registry.exists() else []
    # El worker busca y verifica una carga previa en Odoo; no confiar únicamente
    # en la caché local porque el adjunto podría haber cambiado o desaparecido.
    request={'operation':'upload_image','file':str(path),'name':('COMPUSUR-prueba-privada-' if relative.startswith('tests/') else 'COMPUSUR-')+path.name,'public':public}
    with tempfile.TemporaryDirectory(prefix='compusur-image-request-') as temporary:
        payload=Path(temporary)/'request.json'
        payload.write_text(json.dumps(request,ensure_ascii=False),encoding='utf-8')
        result=subprocess.run(['powershell.exe','-NoProfile','-File',str(ROOT/'scripts/odoo_image_worker.ps1'),'-RequestPath',str(payload)],capture_output=True,text=True,encoding='utf-8',timeout=120)
    try:response=json.loads(result.stdout.strip())
    except json.JSONDecodeError:raise RuntimeError('No se obtuvo una respuesta válida; no reintentar automáticamente.')
    if result.returncode or not response.get('success'):raise RuntimeError(response.get('error','Carga fallida; revisar antes de reintentar.')+' Etapa: '+str(response.get('stage'))+'; adjunto: '+str(response.get('created_id'))+'; HTTP: '+str(response.get('http_status')))
    response['source']=relative
    records=[record for record in records if record.get('id')!=response['id']]
    records.append(response)
    registry.parent.mkdir(exist_ok=True)
    registry.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return response

def serve():
    sys.stdin.reconfigure(encoding='utf-8');sys.stdout.reconfigure(encoding='utf-8')
    for line in sys.stdin:
        request={}
        try:
            request=json.loads(line)
            method=request.get('method');identifier=request.get('id')
            if identifier is None:continue
            if method=='initialize':
                result={'protocolVersion':request.get('params',{}).get('protocolVersion','2024-11-05'),'capabilities':{'tools':{}},'serverInfo':{'name':'compusur-images','version':'1.0.0'}}
            elif method=='ping':result={}
            elif method=='tools/list':result={'tools':[TOOL]}
            elif method=='tools/call':
                parameters=request.get('params',{})
                if parameters.get('name')!=TOOL['name']:raise ValueError('Herramienta no permitida')
                response=upload(parameters.get('arguments',{}))
                result={'content':[{'type':'text','text':json.dumps(response,ensure_ascii=False)}],'isError':False}
            else:
                print(json.dumps({'jsonrpc':'2.0','id':identifier,'error':{'code':-32601,'message':'Método no disponible'}}),flush=True)
                continue
            print(json.dumps({'jsonrpc':'2.0','id':identifier,'result':result},ensure_ascii=False),flush=True)
        except Exception as error:
            message=str(error) if isinstance(error,(ValueError,RuntimeError)) else 'Fallo local de carga; no reintentar sin revisar.'
            print(json.dumps({'jsonrpc':'2.0','id':request.get('id') if isinstance(request,dict) else None,'result':{'content':[{'type':'text','text':message}],'isError':True}},ensure_ascii=False),flush=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upload',help='Ruta local a cargar en privado; sin este argumento inicia MCP')
    parser.add_argument('--public',action='store_true',help='Recurso accesible para web; no publica páginas')
    args=parser.parse_args()
    if args.upload:print(json.dumps(upload({'file':args.upload,'public':args.public}),ensure_ascii=False,indent=2))
    else:serve()

if __name__=='__main__':main()
