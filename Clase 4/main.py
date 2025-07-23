#Paso 1: importar la libreria para comunicarnos con internet (peticiones)
import requests  

#Paso 2: recolectamos  cada dato y lo guardamos en su propia variable
nombre = input("Ingrese su nombre:")
fecha = input("Ingrese la fecha: ")
email = input("Ingrese su email: ")

#Paso 3: definimos la url del webhook
url_webhook = "https://hook.us2.make.com/2r6q6tc65mpy0c2n5v9k2gv0oh74gt35"

#Paso 4: organizamos los datos en diccionario (clave valor)
datos_a_enviar = {
    "name": nombre,
    "startDate": fecha,
    "email": email,
}

#Paso 5: enviamos los datos al webhook
print("Enviando informacion")
#le damos los dos datos que necesita request para hacer un post
respuesta = requests.post(url=url_webhook, json=datos_a_enviar)

#Paso 6: Mostramos la respuesta del servidor
print(f"Status: {respuesta.status_code}")
print(f"Respuesta del servidor: {respuesta.text}")  #pasa a texto la respuesta del servidor