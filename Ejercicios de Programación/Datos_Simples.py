# print("EJERCICIO 5")
# horas = int(input("Ingrese el número de horas trabajadas: "))
# costo = int(input("Ingrese el coste por hora trabajada: "))
# print(f"La paga correspondida es: ${horas * costo}")


# print("EJERCICIO 6")
# n = int(input("Ingrese un entero positivo: "))
# suma = n * (n + 1) / 2
# print(suma) 


# print("EJERCICIO 7")
# print("Vamos a calcular tu Indice de Masa Corporal :)")
# peso = (input("Ingrese su peso (en KG): "))
# altura = (input("Ingrese su altura (Metros): "))
# imc = peso / (altura * altura)
# print(f"Tu índice de masa corporal es {imc}")


# print("EJERCICIO 8")
# m = int(input("Ingrese un número: "))
# n = int(input("Ingrese otro numero: "))
# cociente = m / n
# resto = m % n
# print(f"{m} / {n} = {cociente}\nResto = {resto}")


# print("EJERCICIO 9")
# print("CALCULADORA DE INVERSIONES")
# ingreso = float(input("Ingrese la cantidad a invertir ($) : "))
# interes = float(input("Ingrese el interés anual (%): "))
# años = int(input("Ingrese la cantidad de año/s a invertir: "))
# resultado = (ingreso + (ingreso * interes / 100)) * años
# print(f"El capital que se obtiene por esta inversión es de ${resultado}")


# print("EJERCICIO 10")
# cantidad_payasos = int(input("Ingrese la cantidad de payasos del último pedido: "))
# cantidad_muñecas = int(input("Ingrese la cantidad de muñecas del ultimo pedido: "))
# print(f"El peso total del paquete a enviar es de: {(cantidad_muñecas * 75) + (cantidad_payasos * 112)} gramos")


# print("EJERCICIO 11")
# ahorro = float(input("Ingrese la cantidad de ahorros depositados: "))
# interes = 0.04
# primer_año =  ahorro * (1 + interes)
# segundo_año = primer_año * (1 + interes)
# tercer_año = segundo_año * (1 + interes)
# print(f"Ahorro depositado = ${ahorro}")
# print(f"Intereses del primer año: ${primer_año:.2f}")
# print(f"Intereses del segundo año: ${segundo_año:.2f}")
# print(f"Intereses del tercer año: ${tercer_año:.2f}")


print("EJERCICIO 12")
precio = 3.49
descuento = precio * 0.6
print("Compra de panes:")
pan = int(input("Ingrese la cantidad de panes no frescos vendidos: "))
precio_habitual = precio * pan
descuento_actual = descuento * pan
coste_total = (precio * pan) - (descuento * pan)
print(f"Precio del pan habitual.....${precio_habitual:.2f}")
print(f"Descuento...................${descuento_actual:.2f}")
print(f"Coste total.................${coste_total:.2f}")