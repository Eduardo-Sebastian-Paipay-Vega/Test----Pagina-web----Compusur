$ErrorActionPreference='Stop'
$configPath=Join-Path $env:USERPROFILE '.codex/config.toml'
$serverPath=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot 'odoo_images_mcp.py')).Replace('\','/')
$pythonPath=(Get-Command python -ErrorAction Stop).Source.Replace('\','/')
$current=[IO.File]::ReadAllText($configPath)
if($current -match '(?m)^\[mcp_servers\.odoo_compusur_images\]'){
    Write-Host 'El MCP de imagenes ya esta registrado; no se modifica la entrada existente.'
    exit 0
}
$backup=$configPath+'.before-images-'+(Get-Date -Format 'yyyyMMdd-HHmmss')+'.bak'
Copy-Item -LiteralPath $configPath -Destination $backup
$section=@"

[mcp_servers.odoo_compusur_images]
command = "$pythonPath"
args = ["$serverPath"]
startup_timeout_sec = 60
tool_timeout_sec = 180
enabled = true
"@
[IO.File]::WriteAllText($configPath,$current.TrimEnd()+"`r`n"+$section+"`r`n",(New-Object Text.UTF8Encoding($false)))
Write-Host 'MCP de imagenes registrado. El MCP general conserva modo lectura.'
Write-Host 'Reinicia Codex para cargar upload_website_image.'
