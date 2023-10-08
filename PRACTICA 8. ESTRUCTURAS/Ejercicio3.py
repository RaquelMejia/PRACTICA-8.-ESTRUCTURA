try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo 'archivo_inexistente.txt' no existe. Por favor, ingresa un dato correcto.")
