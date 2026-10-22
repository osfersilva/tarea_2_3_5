def calcular_promedio(*args):
    # Operador ternario: verifica si hay al menos 2 argumentos
    return sum(args) / len(args) if len(args) >= 2 else "\nError: No se pasaron suficientes argumentos (mínimo 2).\n"

entrada = input("\nIngresá al menos dos números separados por espacio: ").split()
numeros = [float(n) for n in entrada]

resultado = calcular_promedio(*numeros)
print(f"\nEl promedio es: {resultado}\n")