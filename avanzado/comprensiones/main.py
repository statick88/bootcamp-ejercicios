# # Comprension de lista
# cuadrados = [x**2 for x in range(5)]
# print(cuadrados)

#Generadores
# def contador():
#     for i in range(5):
#         valor = yield i**2
#         print(f"Valor recibido: {valor}")

# contador = contador()
# print(next(contador))
# print(next(contador))
# print(next(contador))

# gen = contador()
# for valor in gen:
#     print(valor)

nombres = ["Maria", "Juan", "Pedro", "Luis"]
longitudes = {nombre: len(nombre) for nombre in nombres}
print(longitudes)