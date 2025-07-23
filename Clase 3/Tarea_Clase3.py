# """
# **Consigna: "Mini Agenda de Contactos"**
# 1. Crea una lista vacía llamada agenda.
# 2. Pide al usuario que ingrese el nombre y el teléfono de 2 personas.
# 3. Por cada persona, crea una tupla (nombre, telefono) y añádela a tu lista agenda.
# 4. Una vez ingresados los datos, recorre la lista agenda.
# Para cada contacto en la agenda, muestra un mensaje formateado con f-string, por ejemplo: "Contacto:[Nombre], Teléfono: [Telefono]"
# """


# print("======================================")
# print("             Mi agenda                ")
# print("======================================")

# #Crear lista vacia
# agenda = []

# #Input de datos
# for i in range(2):
#     nombre = input("Ingrese el nombre del contacto: ")
#     telefono = int(input("Ingrese el número de teléfono: "))
#     agregar = (nombre, telefono)  #Creo una tupla en una variable temporal
#     agenda.append(agregar)  #Agrego la tupla a la lista

# for contacto in agenda:
#     nombre_mostrar, telefono_mostrar = contacto
#     print(f"Contacto: {nombre_mostrar}, Telefono: {telefono_mostrar}")



"""
**Consigna: "Analizador de Frases"**
Escribe un programa que haga lo siguiente:
    1. Pida al usuario que ingrese una frase.
    2. Muestre la frase en **mayúsculas**.
    3. Divida la frase en una lista de palabras usando el método .split().
    4. Muestre cuántas palabras tiene la frase.Muestre la primera y la última palabra de la frase.
"""
print("======================================")
print("         Analizador de Frases         ")
print("======================================")

#Input de frase
frase = input("Ingrese una frase: ")

#Frase en mayúsculas
frase_mayuscula = frase.upper()
print("Convirtiendo caracteres a mayúsculas...")
print(frase_mayuscula)

#Separar frase con .split()
print("Descuartizando frase...")
frase_descuartizada = frase.split()
print(frase_descuartizada)

#Conteo de palabras
print(f"La frase '{frase}' contiene {len(frase_descuartizada)} palabras")
print(f"La primera palabra es: {frase_descuartizada[0]}")
print(f"La última palabra es: {frase_descuartizada[-1]}")