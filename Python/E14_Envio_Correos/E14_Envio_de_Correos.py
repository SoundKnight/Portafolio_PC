# --- <=> INTENGRANTES <=> ---
# Ibrahim Zavala Hernandez 
# Julio Gerardo Cazarez Gonzalez 
# Pedro Saldaña Vazquez 

# ---<=> MODULOS <=>---
import ssl
import smtplib
import getpass
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# ---<=> SCRIPT <=>---
print("<=><=><=> ENVIO DE CORREOS <=><=><=>")
print("--- CORREO DEL EMISOR ---")
emisor = input("Ingrese su Correo Electronico: ")
contraseña = getpass.getpass("Ingrese su Contraseña: ")
print("\n--- CORREO DEL RECEPTOR ---")
receptor = input("Ingrese el Correo del Destino: ")
print("\n--- INFORMACION DEL MENSAJE ---")
asunto = input("Ingrese el Asunto del Mensaje: ")
mensaje = input("Ingrese el Mensaje: ")
imagen = input("Ingrese la Ruta de la Imagen: ")

try: 
    correo = MIMEMultipart()
    correo["Subject"] = asunto
    correo["From"] = emisor
    correo["To"] = receptor
    correo["body"] = mensaje

    correo.attach(MIMEText(mensaje, "plain"))

    with open(imagen,'rb') as attachment:
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {imagen}")
    correo.attach(part)
    text = correo.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP("outlook.office365.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(emisor, contraseña)
        server.sendmail(
            emisor, receptor, correo.as_string()
        )
    print("\n*** CORREO ENVIADO EXITOSAMENTE ***")
    input("Presione ENTER para Salir")
    
except Exception as e:
    print("Error", e)


""