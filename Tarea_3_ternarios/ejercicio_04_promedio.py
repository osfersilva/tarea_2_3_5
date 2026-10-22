def calcular_promedio(*args):
    # Operador ternario para calcular el promedio solo si hay elementos, de lo contrario devuelve 0
    return sum(args) / len(args) if len(args) > 0 else 0 

# Ingreso de números por teclado
entrada = input ("\nIngresá los números separados por espacio: ").split()
numeros = [float(n) for n in entrada]

# Llamada a la función usando el operador de desempaquetado (*)
resultado = calcular_promedio(*numeros)

print(f"\nEl promedio es: {resultado}\n") 