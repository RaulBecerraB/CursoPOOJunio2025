from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self,area):
        self.area = area
        
    @abstractmethod
    def calcular_area(self):
        pass
    
    