"""
Ejercicio 2: Generador de Nombres de Usuario
Escribe un programa que:
1. Pida al usuario su nombre, su apellido y su año de nacimiento.
2. Cree un nombre de usuario combinando las primeras 3 letras del nombre, las primeras 3 letras del apellido y los últimos 2 dígitos del año de nacimiento.
3. Muestre el nombre de usuario sugerido, convertido completamente a minúsculas.
○ Ejemplo: Para Ana García nacida en 2005, el resultado debe ser anagar05.
"""

print("---------------------------------")
print("      Generador de Username      ")
print("---------------------------------")
nombre = input("Bienvenido!\nIngrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nacimiento = input("Ingrese su año de nacimiento: ")
print("\nGenerando nombre de usuario...")
username = nombre[0] + nombre[1] + nombre[2] + apellido[0] + apellido[1] + apellido[2] + nacimiento[-2] + nacimiento[-1]
print(f"\nNombre de usuario sugerido: {username.lower()}") 