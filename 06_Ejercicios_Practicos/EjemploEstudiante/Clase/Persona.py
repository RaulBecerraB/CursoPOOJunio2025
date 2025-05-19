class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # Usamos _edad como atributo privado
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa") 
        self._edad = nueva_edad
    
    @edad.getter
    def obtener_edad(self):
        return self._edad
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self._edad, "años")
    
    def es_mayor_de_edad(self):
        if self._edad >= 18:
            print("Soy mayor de edad")
        else:
            print("Soy menor de edad")