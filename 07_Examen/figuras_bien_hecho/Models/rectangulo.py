from .figura import Figura

class Rectangulo(Figura):
    """Clase que representa un rectángulo."""
    
    def __init__(self, ancho: float, alto: float):
        """Inicializa un rectángulo con ancho y alto.
        
        Args:
            ancho (float): El ancho del rectángulo
            alto (float): El alto del rectángulo
        """
        self._ancho = ancho
        self._alto = alto

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo.
        
        Returns:
            float: El área calculada
        """
        return self._ancho * self._alto 