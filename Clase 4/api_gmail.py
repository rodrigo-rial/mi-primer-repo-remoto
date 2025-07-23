import requests

print("Que onda putito")
correo = input("Ingresa el destinatario: ")
mensaje = input("Ingresa el mensaje de los cojones: ")

url_webhook = "https://hook.us2.make.com/ti8pg5ct7qaxpyfqt7841gah8ksfsspo"

datos_a_enviar = {
    "email": correo,
    "message": mensaje
}

print("Enviando mail")
respuesta = requests.post(url = url_webhook, json = datos_a_enviar)
print(f"Status: {respuesta.status_code}")
print(f"Respuesta del servidor: {respuesta.text}")
print("Mail enviado exitosamente")