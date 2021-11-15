# --- <=> INTENGRANTES <=> ---
# Ibrahim Zavala Hernández 
# Julio Gerardo Cazarez González 
# Pedro Saldaña Vázquez 

# --- <=> MODULOS <=> ---
import argparse
import cifrado
import descifrado
import crackeo

# --- <=> ARGUMENTOS <=> ---
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, dest='modo', help='Eleccion de Modo: encriptar || desencriptar || crackear')
parser.add_argument('--message', type=str, dest='mensaje', help='Mensaje a Encriptar || Desencriptar || Crakear')
parser.add_argument('--key', type=str, dest='clave', default='ClaveDefault', help='(Opcional) Clave para Encriptar || Desencriptar')
args=parser.parse_args()

if args.modo == 'encriptar':
    print("\n--- <=> ENCRIPTACION DE MENSAJE <=> ---")
    mensaje = args.mensaje
    ckey = args.clave
    cifrado.encriptado(mensaje, ckey)
elif args.modo == 'desencriptar':
    print("\n--- <=> DESENCRIPTACION DE MENSAJE <=> ---")
    mensaje = args.mensaje
    ckey = args.clave
    descifrado.desencriptado(mensaje, ckey)
elif args.modo == 'crackear':
    print("\n--- <=> CRACKEO DE MENSAJE <=> ---")
    mensaje = args.mensaje
    crackeo.crackeado(mensaje)

else:
    print("usage: MainScript.py [-h] [--mode MODO] [--message MENSAJE] [--key CLAVE]")