import requests
url = "https://v2.jokeapi.dev/joke/Any?lang=es&type=twopart"
#url = "https://v2.jokeapi.dev/joke/Programming?lang=en"
respuesta = requests.get(url)


#condicional de status
if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos["type"] == "single":
        print("Chiste:", datos["joke"])
    else:
        print("Chiste:", datos["setup"])
        print("Remate:", datos["delivery"])
else:
    print("Error al obtener el chiste.")