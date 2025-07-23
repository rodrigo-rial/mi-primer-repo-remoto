"""
Objetivo: El usuario ingresa su nombre, CUIT, monto y email. Python envía los datos por POST.
Make.com crea un documento PDF con los datos (por ejemplo con Google Docs).
Se guarda en Google Drive.
Se envía por correo al usuario.
"""
import requests

print("-----------------------------------")
print("       Generador de Facturas       ")
print("-----------------------------------")
nombre = input("Ingrese el nombre: ")
cuit = (input("Ingrese el CUIT: "))
monto = (input("Ingrese el monto: "))
mail = input("Ingrese el mail: ")

datos_a_enviar = {
    "nombre": nombre,
    "cuit": cuit,
    "monto": monto,
    "mail": mail
}

url_webhook = "https://hook.us2.make.com/qv3gvhfp7bgaqzlk8ug7t59yqw0giqct"
respuesta = requests.post(url = url_webhook, json = datos_a_enviar)

print(f"Respuesta del servidor: {respuesta.status_code}")