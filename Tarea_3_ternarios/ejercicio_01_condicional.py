# Entrada de datos desde el teclado
num1 = float(input("\nIngrese el primer número: "))
num2 = float(input("\nIngrese el segundo número: "))

# Operador ternario para encontrar el mayor
mayor = num1 if num1 > num2 else num2

print(f"\nEl mayor número es: {mayor}\n")