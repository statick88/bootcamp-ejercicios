# POO Persona

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def seludar(self):
        return(f"Hola, mo nombre es {self.nombre} y tengo {self.edad} años")
    
persona1 = Persona("Diego", 36)
print(persona1.nombre)
print(persona1.edad)
print(persona1.seludar())

persona2 = Persona("Maria", 45)
print(persona2.nombre)
print(persona2.edad)
print(persona2.seludar())
