# """
# Crea una lista vacía llamada playlist.
# Pide al usuario que ingrese 3 nombres de canciones y añádelas a la lista usando append().
# Muestra la playlist completa.
# Muestra cuántas canciones hay en la playlist.
# Pregunta al usuario qué canción quiere eliminar y quítala de la lista usando .remove().
# Muestra la playlist final.
# """

# #Lógica 
# """
# 1. []
# 2. tengo que tener un input que va a pedir 3 canciones y uso append para agregar
# 3. print
# 4. tengo que meter un len
# 5. pedir al user cual eliminar y usar .remove()
# 6. print lista
# """
# #1
# playlist = []

# #2
# cancion1 = input("Ingrese el nombre de la primer cancion: ").lower()
# playlist.append(cancion1)
# cancion2 = input("Ingrese el nombre de la segunda cancion: ").upper
# playlist.append(cancion2)
# cancion3 = input("Ingrese el nombre de la tercer cancion: ").capitalize
# playlist.append(cancion3)

# #3
# print(playlist)

# #4
# print(f"La playlist tiene {len(playlist)} canciones")

# #5
# cancion_eliminar = input("Ingrese la cancion que desee eliminar: ")
# playlist.remove(cancion_eliminar)

# #6
# print(playlist)

# coordenadas = (1920, 1080, "full hd")
# # Desempaquetado
# ancho, alto, calidad = coordenadas  #Asignación múltiple -> asigno varios valores al mismo tiempo
# print(f"Ancho de la pantalla: {ancho}px")
# print(f"Alto de la pantalla: {alto}px")
# print(f"Alto de la pantalla: {calidad}px")

# # También funciona en bucles for con listas de tuplas
# usuarios = [("juanperez", "juan@email.com"), ("ana_g", "ana@email.com")]
# for usuario, email in usuarios:
#     print(f"Procesando a {usuario} con email {email}")

# lenguaje = "Python"
# # Acceso y slicing
# print(lenguaje[0])    # P
# print(lenguaje[-1])   # n
# print(lenguaje[1:4])  # yth El ultimo valor no lo tóma, es un intervalo '[ )'
# # ¡Esto daría un error! Las cadenas son inmutables.
# #lenguaje[0] = "J"

# print(lenguaje[:])  #Devuelve una copia
# print(lenguaje[:5])  #Pytho  start-stop
# print(lenguaje[1:])  #ython

# lenguaje = "Alejandro sosa es un kpo"
# print(lenguaje[1:10:3])    #del 1 al 10, de 2 en dos (llamado step) start - stop - step 
