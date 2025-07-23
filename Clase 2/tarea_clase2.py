numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

#Toma dos operandos y devuelve la suma de sus valores
suma = numero1 + numero2
print("---------------------------------------")
print(f"Suma = {numero1} + {numero2} = {suma} ")
print("---------------------------------------")

#Resta el segundo operando del primero
resta = numero1 - numero2
print(f"Resta = {numero1} - {numero2} = {resta}")
print("---------------------------------------")

#Multiplica los dos operandos
multiplicacion = numero1 * numero2
print(f"Multiplicacion = {numero1} * {numero2} = {multiplicacion}")
print("---------------------------------------")

#Divide el primer operando por el segundo y devuelve un resultado flotante
division = numero1 / numero2
print(f"Division = {numero1} / {numero2} = {division}")
print("---------------------------------------")

#Divide el primer operando por el segundo y devuelve la parte entera del resultado
division_entera = numero1 // numero2
print(f"Division entera = {numero1} // {numero2} = {division_entera}")
print("---------------------------------------")

#Devuelve el resto de la división del primer operando por el segundo
modulo = numero1 % numero2
print(f"Modulo = {numero1} % {numero2} = {division_entera}")
print("---------------------------------------")

#Eleva el primer operando a la potencia del segundo
potencia = numero1 ** numero2
print(f"Potencia = {numero1} ** {numero2} = {potencia}")