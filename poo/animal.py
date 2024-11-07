# POO - Animal

class Animal:

    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def comer(self):
        return(f"El animal {self.nombre} tiene aproximadamente {self.edad} años y es de la especie {self.especie}, actualmente esta comiendo")
    
    def __del__(self):
        print(f"El animal {self.nombre} ha sido eliminado")

gato = Animal("Pepito", "2", "gato")
print(gato.comer())

perro = Animal("Juanita", "1", "perro")
print(perro.comer())
del perro, gato

