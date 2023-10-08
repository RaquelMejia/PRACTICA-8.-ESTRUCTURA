nombres = []
while True:
    nombre = input("Por favor, ingresa un nombre (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    nombres.append(nombre)

with open('nombres.txt', 'w') as archivo:
    
    for nombre in nombres:
        archivo.write(nombre +'\n')