from operaciones import suma as s, resta, multiplicacion, division

num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))

print(f"La suma de {num1} y {num2} es: {s(num1, num2)}")
print(f"La resta de {num1} y {num2} es: {resta(num1, num2)}")
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion(num1, num2)}")
print(f"La division de {num1} y {num2} es: {division(num1, num2)}")
