from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self,area):
        self.area = area
        
    @abstractmethod
    def calcular_area(self):
        print("no hay fórmula para calcular el área")
        pass
    
    