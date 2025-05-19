from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  # Llamamos al constructor de Persona
        self.matricula = matricula
           
    def decirMatricula(self):
        print("Mi matricula es ", self.matricula)
        
    def estudiar(self):
        print("Estoy estudiando")
        
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, nueva_matricula):
        self._matricula = nueva_matricula

