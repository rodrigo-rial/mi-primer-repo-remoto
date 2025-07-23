"""
Ejercicio 1: Calculadora de Propinas
Escribe un programa que:
1. Pregunte al usuario el monto total de la cuenta (ej: 2550.50).
2. Pregunte qué porcentaje de propina le gustaría dejar (ej: 10).
3. Calcule el monto exacto de la propina y el total final de la cuenta (monto original + propina).
4. Muestre por pantalla un mensaje claro que indique el monto de la propina y el total a pagar.
"""

print("---------------------------------")
print("     Calculadora de propinas     ")
print("---------------------------------")
monto_original = float(input("Bienvenido!\nIngrese el monto total de la cuenta: "))
propina = int(input("Indique el porcentaje de propina que desea dejar (%): "))
propina_final = monto_original * propina / 100
monto_final = monto_original + propina_final
print("---------------------------------")
print(f"Monto original.....${monto_original:.2f}")
print(f"Propina............${propina_final:.2f}")
print(f"Total..............${monto_final:.2f}")