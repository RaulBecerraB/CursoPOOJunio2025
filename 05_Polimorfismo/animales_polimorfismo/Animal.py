from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,nombre,edad,color):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        
    @abstractmethod
    def hacer_sonido(self):
        pass