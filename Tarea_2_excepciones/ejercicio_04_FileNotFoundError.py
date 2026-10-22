try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)

except FileNotFoundError:
    print("\nError: El archivo no existe. Se procederá a crearlo.")
    with open("archivo_inexistente.txt", "w") as archivo_nuevo:
        archivo_nuevo.write("Este es un archivo creado automáticamente.")
    print("\n¡Archivo creado con éxito!\n")