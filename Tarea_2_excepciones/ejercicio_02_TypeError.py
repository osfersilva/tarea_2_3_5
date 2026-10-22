try:
    numero = int(input("\nIngresá un número: "))
    cadena = input("\nIngresá una cadena de texto: ")
    
    # Intentamos sumar un entero y una cadena (lo cual genera un TypeError)
    resultado = numero + cadena
    print(f"\nEl resultado es: {resultado}\n")

except TypeError:
    print("\nError: No se puede sumar un número y una cadena de texto.\n")