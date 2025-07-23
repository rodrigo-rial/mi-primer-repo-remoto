"""
Ejercicio 1: Registro de Inscripción a un Taller
Objetivo: El usuario completa su nombre, email y curso de interés. 
Se envía vía POST a Make.com, que:
Guarda la info en Google Sheets.
Envía un correo de confirmación al inscripto.
"""
import requests


print("-----------------------------------")
print("       Inscripción a Taller        ")
print("-----------------------------------")
nombre = input("Ingrese su nombre y apellido: ")
mail = input("Ingrese su mail: ")
curso = input("Ingrese su curso de interés: ")

datos_a_enviar = {
    "name":nombre,
    "email":mail,
    "curso":curso
}

url_webhook = "https://hook.us2.make.com/zijpzkxil9orjt07axvkuy92e6ttpmpg"
respuesta = requests.post(url = url_webhook, json = datos_a_enviar)

print("Enviando datos...")
print(f"Respuesta del servidor: {respuesta.status_code}")
