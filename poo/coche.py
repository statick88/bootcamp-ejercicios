# Programacion Orientada a Objetos - POO

class Coche:
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        return (f"El coche {self.marca} {self.modelo} de color {self.color} esta acelerando")
    
    def frenar(self):
        return (f"El conche {self.marca} {self.modelo} de color {self.color} esta frenando")
    
    def __str__(self):
        return (f"Coche {self.marca} {self.modelo} de color {self.color}")

coche = Coche("Toyota", "Corola", "Rojo")
print(coche.marca)
print(coche.modelo)
print(coche.color)

print(coche.acelerar())
print(coche.frenar())

print(coche.__str__())