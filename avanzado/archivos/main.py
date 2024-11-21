# # Escritura de archivo
# with open('archivo.txt', 'w') as f:
#     f.write("Hola mundo developers!\n")

# # Lectura de archivo
# with open('archivo.txt', 'r') as f:
#     contenido = f.read()
#     print(contenido)

# with open('python_logo.png', "r") as file:
#     datos = file.read()

with open("saludo.txt", "w") as file:
    file.write("Hola, mundo")

with open("saludo.txt", "r") as file:
    for linea in file:
        print(linea.strip())