mi_diccionario = {"nombre": "Ana", "edad": 25}

try:
    # Intentamos acceder a una clave que no existe en el diccionario
    valor = mi_diccionario["telefono"]
    print(valor)

except KeyError:
    print("\nError: La clave especificada no existe en el diccionario.\n")