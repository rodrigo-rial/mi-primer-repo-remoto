"""
Ejercicio 4: Registro de Puntos de un Juego
Escribe un programa que:
1. Cree una lista de tuplas donde cada tupla contenga el nombre de un jugador y su puntaje. Debes incluir al menos 3 jugadores. 
    ○ Ejemplo: [("Ana", 1500), ("Juan", 1250), ("Caro", 1800)]
2. Recorra la lista e imprima un mensaje para cada jugador, usando el desempaquetado de tuplas, que diga: "El jugador [Nombre] alcanzó [Puntaje] puntos."
"""
lista = []
for i in range(3):
    nombre = input("Ingrese el nombre del jugador: ")
    puntaje = int(input("Ingrese el puntaje: "))
    tupla = (nombre, puntaje)
    lista.append(tupla)
    print(f"jugador {i + 1} agregado.\n")

for jugador in lista:
    nombre, puntos = jugador
    print(f"El jugador {nombre} alcanzó {puntos} puntos.")