#neHXadRJj9Acv-t API KEY
# 9@sCfJgKTCMaBhM WPP KEY
import requests

#Recolectamos la informacion
contacto = "1170451697"
mensaje = input("Ingrese el mensaje que quiere mandarle a mica: ")

#Definimos la URl del webhook
url_webhook = "https://hook.us2.make.com/gu3ywnxunql252lw9c5aechkhbt9u3l8"

#Organizamos los datos en el dic
datos_a_enviar = {
    "contact":contacto,
    "message": mensaje
}

#Enviamos los datos al webhook
print("Enviando mensaje")
respuesta = requests.post(url = url_webhook, json = datos_a_enviar)

#Mostramos respuesta del servidor
print(f"Status: {respuesta.status_code}")
print(f"Respuesta del servidor: {respuesta.text}")