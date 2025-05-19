class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print("Hola, mi nombre es", self.nombre, "y mi edad es", self.edad)
    
    def esMayorDeEdad(self):
        if self.edad >= 18:
            print("Soy mayor de edad")
        else:
            print("Soy menor de edad") 