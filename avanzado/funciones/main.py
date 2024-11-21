from functools import reduce

# Uso de lambda y map
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x*2, numeros))
print(dobles)

# Uso de filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 == 1, numeros))
print(pares)
print(impares)

# Uso de reduce
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

from math import sqrt
sqrt = sqrt(9)
print(sqrt)