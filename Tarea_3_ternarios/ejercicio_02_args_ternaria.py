def buscar_en_lista(palabra, *args):
    # Uso del operador ternario evaluando si la palabra está dentro de los *args
    return f"\nLa palabra '{palabra}' SÍ está en los argumentos.\n" if palabra in args else f"\nLa palabra '{palabra}' NO está en los argumentos.\n"

def main():
    # 1. Ingresar la palabra a buscar por teclado
    palabra_buscada = input("\nIngresá la palabra que querés buscar: ").strip()

    # 2. Ingresar los elementos por teclado y pasarlos como *args usando el operador de desempaquetado (*)
    entrada_usuario = input("\nIngresá las palabras separadas por espacio: ").split()
    
    # 3. Llamar a la función pasando la palabra y los elementos expandidos como *args
    resultado = buscar_en_lista(palabra_buscada, *entrada_usuario)

    # 4. Mostrar el resultado final
    print(resultado)

if __name__ == "__main__":
    main()