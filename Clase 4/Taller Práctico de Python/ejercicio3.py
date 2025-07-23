"""
Ejercicio 3: Gestionando la Lista de Compras
Escribe un programa que realice las siguientes acciones:
1. Crea una lista inicial con tres productos: ["Leche", "Pan", "Huevos"].
2. Pide al usuario que ingrese un nuevo producto, y añádelo al final de la lista.
3. Pide al usuario que ingrese otro producto, pero esta vez añádelo al principio de la lista.
4. Muestra por pantalla la lista actualizada y la cantidad total de productos que contiene.
5. Ordena la lista alfabéticamente y muéstrala.
6. Finalmente, pregunta al usuario qué producto desea eliminar y quítalo de la lista. 
Muestra la lista final.
"""

print("----------------------------------")
print("         Lista de Compras         ")
print("----------------------------------")

lista = ["Leche", "Pan", "Huevos"]
print(lista)
producto1 = (input("Ingrese un nuevo producto: ")).capitalize()
print("Añadiendo al final de la fila...")
lista.append(producto1)
print(lista)

producto2 = (input("\nIngrese otro producto: ")).capitalize()
print("Añadiendo al principio de la fila...")
lista.insert(0, producto2)
print(lista)

print("\nOrdenando lista...")
lista.sort()
print(lista)

producto_eliminar = input("\n¿Qué producto desea eliminar?: ")
print("Eliminando producto...")
lista.remove(producto_eliminar)
print(lista)