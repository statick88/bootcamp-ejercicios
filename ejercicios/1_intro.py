# Ejercicios
"""
1. Crear un ejercicio que me permita saber si una persona es mayor
de edad.
"""





# Solicitar el año de nacimiento al usuario
anio_nacimiento = int(input("¿Cuál es tu año de nacimiento? (AAAA): "))

# Obtener el año actual
anio_actual = 2024

# Calcular la edad
edad = anio_actual - anio_nacimiento

# Imprimir resultado
print("Eres mayor de edad." * (edad >= 18) + "No eres mayor de edad." * (edad < 18))