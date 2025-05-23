import math
from .figura import Figura

class Circulo(Figura):
    """Clase que representa un círculo."""
    
    def __init__(self, radio: float):
        """Inicializa un círculo con un radio.
        
        Args:
            radio (float): El radio del círculo
        """
        self._radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo.
        
        Returns:
            float: El área calculada
        """
        return math.pi * (self._radio ** 2) 