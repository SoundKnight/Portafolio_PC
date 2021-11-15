# ---Autores:  MARCO ARTURO CANTU VIVANCO, PEDRO SALDAÑA VAZQUEZ,
# GERARDO GAMEZ SERNA, IBRAHIM ZAVALA HERNANDEZ---
from pyhunter import PyHunter
from openpyxl import Workbook
import getpass


# Cantidad de resultados esperados de la búsqueda
def Busqueda(organizacion):
    resultado = hunter.domain_search(company=organizacion, limit=1,
                                     emails_type='personal')
    return resultado


# Escribe datos relevantes en una hoja de Excel
def GuardarInformacion(datosEncontrados, organizacion):
    libro = Workbook()
    hoja = libro.create_sheet(organizacion)
    hoja = libro.active
    hoja["A1"] = "País"
    hoja["A2"] = datosEncontrados['country']
    hoja["B1"] = 'Estado'
    hoja["B2"] = datosEncontrados['state']
    hoja["C1"] = "Dominio"
    hoja["C2"] = datosEncontrados['domain']
    hoja["D1"] = "Es desechable?"
    hoja["D2"] = datosEncontrados['disposable']
    hoja["E1"] = "Es webmail?"
    hoja["E2"] = datosEncontrados['webmail']
    hoja["F1"] = "Correo encontrado"
    hoja["F2"] = correo1['value']
    libro.save("Hunter" + organizacion + ".xlsx")
print("Script para buscar información ")
apikey = getpass.getpass(" Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datosEncontrados = Busqueda(orga)
if datosEncontrados is None:
    exit()
else:
    print(datosEncontrados)
    print(type(datosEncontrados))
# Extraemos el email que está dentro de un diccionario dentro de una lista
# dentro del diccionario con los resultados
    correos = datosEncontrados['emails']
    correo1 = correos[0]
    GuardarInformacion(datosEncontrados, orga)