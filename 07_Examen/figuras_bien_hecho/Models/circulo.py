import math
from .figura import Figura

class Circulo(Figura):
    """Clase que representa un círculo."""
    
    def __init__(self, radio: float):
        """Inicializa un círculo con un radio.
        
        Args:
            radio (float): El radio del círculo
            
        Raises:
            ValueError: Si el radio no es un número positivo
        """
        if not isinstance(radio, (int, float)) or radio <= 0:
            raise ValueError("El radio debe ser un número positivo")
            
        self._radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo.
        
        Returns:
            float: El área calculada
        """
        return math.pi * (self._radio ** 2) 