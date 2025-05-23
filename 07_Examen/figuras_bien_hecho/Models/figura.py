from abc import ABC, abstractmethod

class Figura(ABC):
    """Interfaz para todas las figuras geométricas."""
    
    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula el área de la figura.
        
        Returns:
            float: El área calculada
        """
        pass 