# Ibrahim Zavala Hernandez
# Julio Gerardo Cazarez Gonzalez
# Pedro Saldaña Vazquez

Import-Module C:\Users\SoundKnight\Desktop\E1PC\E3Funciones.psm1
# --- MENU ---
do{ 
    Write-Host ""
    $opcion = read-host "Que deseas hacer? 
    [1]Ver el estatus de un perfil especifico en el Firewall  
    [2]Cambiar el estatus de los perfiles 
    [3]Ver el perfil de nuestra red 
    [4]Cambiar nuestra red a otro tipo de perfil 
    [5]Ver las reglas de bloqueo 
    [6]Agregar regla de bloqueo de entrada para un puerto 
    [7]Eliminar regla de bloqueo 
    [8]Salir
    Opcion"
        switch ($opcion){
                1{
                    Ver-StatusPerfil
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                }
                2{
                    Cambiar-StatusPerfil
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                }
                3{
                    Ver-PerfilRedActual
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                }
                4{
                    Cambiar-PerfilRedActual
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                    }
                5{
                    Ver-ReglasBloqueo
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                }
                6{
                    Agregar-ReglasBloqueo
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                }
                7{
                    Eliminar-ReglasBloqueo
                    $Pausa = Read-Host "Presiona Enter Para Continuar"
                    break
                }
                8{
                    break
                }
                default{
                    Write-Host "Valor Invalido"
                }  
            }
    } while($opcion -ne 8){  
    }
    
    # --- SALIDA ---
    Write-Host "Fin del Programa"