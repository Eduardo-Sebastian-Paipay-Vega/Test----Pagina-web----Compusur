param([Parameter(Mandatory=$true)][string]$RequestPath)
$ErrorActionPreference='Stop'
$headers=$null;$credential=$null
$stage='preparacion';$id=$null
try {
    $request=[IO.File]::ReadAllText($RequestPath) | ConvertFrom-Json
    if($request.operation -ne 'upload_image'){throw 'Operacion no permitida'}
    $root=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
    $file=[IO.Path]::GetFullPath([string]$request.file)
    $assetRoot=[IO.Path]::GetFullPath((Join-Path $root 'src/assets'))+[IO.Path]::DirectorySeparatorChar
    $testRoot=[IO.Path]::GetFullPath((Join-Path $root 'tests/fixtures'))+[IO.Path]::DirectorySeparatorChar
    if(-not ($file.StartsWith($assetRoot,[StringComparison]::OrdinalIgnoreCase) -or ($file.StartsWith($testRoot,[StringComparison]::OrdinalIgnoreCase) -and -not $request.public))){throw 'Archivo fuera del alcance'}
    $bytes=[IO.File]::ReadAllBytes($file)
    if($bytes.Length -gt 5242880 -or $bytes.Length -eq 0){throw 'Tamano no permitido'}
    $ext=[IO.Path]::GetExtension($file).ToLowerInvariant()
    if($ext -notin @('.png','.jpg','.jpeg','.webp','.svg')){throw 'Formato no permitido'}
    $credential=Import-Clixml -LiteralPath (Join-Path $env:USERPROFILE '.codex/tools/odoo-compusur/credencial.xml')
    $headers=@{Authorization='Bearer '+$credential.GetNetworkCredential().Password;'X-Odoo-Database'=$credential.UserName}
    function Invoke-Odoo($method,$parameters){
        $body=ConvertTo-Json -InputObject $parameters -Depth 12 -Compress
        Invoke-RestMethod -Uri "https://compusur.odoo.com/json/2/ir.attachment/$method" -Method Post -Headers $headers -ContentType 'application/json' -Body $body -TimeoutSec 45
    }
    $binary=[Convert]::ToBase64String($bytes)
    $values=@{name=[string]$request.name;type='binary';raw=$binary;website_id=1;res_model='ir.ui.view';public=[bool]$request.public}
    $stage='buscar_carga_previa'
    $existing=Invoke-Odoo 'search_read' @{domain=@(@('name','=',$values.name),@('website_id','=',1),@('public','=',[bool]$request.public));fields=@('id','raw');limit=10}
    foreach($item in $existing){
        foreach($candidate in $item){if([string]$candidate.raw -ceq $binary){$id=[int]$candidate.id;break}}
        if($id){break}
    }
    if(-not $id){
        $stage='crear_adjunto'
        $created=Invoke-Odoo 'create' @{vals_list=@($values)}
        while($created -is [array]){$created=$created[0]}
        $id=[int]$created
    }
    $stage='leer_adjunto'
    $record=Invoke-Odoo 'read' @{ids=@($id);fields=@('id','name','mimetype','file_size','public','website_id','image_width','image_height','raw');context=@{bin_size=$false}}
    while($record -is [array]){$record=$record[0]}
    $stage='verificar_metadatos'
    if(-not $record.mimetype.StartsWith('image/')){throw 'Odoo no identifico una imagen'}
    if([int]$record.website_id[0] -ne 1 -or [bool]$record.public -ne [bool]$request.public){throw 'Asociacion no coincide'}
    $stage='verificar_binario'
    $downloaded=[Convert]::FromBase64String([string]$record.raw)
    $sha=[Security.Cryptography.SHA256]::Create()
    $sourceHash=[BitConverter]::ToString($sha.ComputeHash($bytes)).Replace('-','').ToLowerInvariant()
    $storedHash=[BitConverter]::ToString($sha.ComputeHash($downloaded)).Replace('-','').ToLowerInvariant()
    if($sourceHash -cne $storedHash){throw 'Imagen almacenada distinta del archivo'}
    @{success=$true;id=$id;name=$record.name;mimetype=$record.mimetype;size=$record.file_size;width=$record.image_width;height=$record.image_height;public=$record.public;website_id=1;sha256=$storedHash;url="/web/image/$id";verified_binary=$true;page_modified=$false} | ConvertTo-Json -Compress -Depth 6 | Write-Output
} catch {
    $status=if($_.Exception.Response){[int]$_.Exception.Response.StatusCode}else{0}
    @{success=$false;http_status=$status;stage=$stage;created_id=$id;error='La carga o verificacion fallo; comprobar el registro de prueba antes de reintentar.'} | ConvertTo-Json -Compress | Write-Output
    exit 1
} finally {$headers=$null;$credential=$null;$binary=$null;$bytes=$null}
