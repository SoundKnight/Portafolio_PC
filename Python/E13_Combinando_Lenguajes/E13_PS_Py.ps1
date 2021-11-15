#Ibrahim Zavala Hernandez, Julio Gerardo Cazares Gonzales, Pedro Saldaña Vazquez

<#El script se debe guardar en la misma carpeta para así no escribir la ruta
completa, en caso que se deseé, se puede modificar el script de python para que
haga ws de otra pagina#>

$Python = "python.exe"

$Script = "webScapping.py"

Write-Host "--Web Scraping para extraer info de imagenes--"

$Message = "Hello Python - Hello World"

$Message | & $Python $Script