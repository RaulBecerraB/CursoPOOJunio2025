from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
    
    def inscribirse_en_curso(self):
        print("Estoy inscribiendome en un curso")