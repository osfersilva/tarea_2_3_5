try:
    num1 = float(input("\nIngresá el primer número: "))
    num2 = float(input("\nIngresá el segundo número: "))
    
    resultado = num1 / num2
    print(f"\nEl resultado es: {resultado}\n")

except ZeroDivisionError:
    print("\nError: No se puede dividir entre cero.\n")