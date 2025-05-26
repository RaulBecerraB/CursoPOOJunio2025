from .figura import Figura

class Rectangulo(Figura):
    """Clase que representa un rectángulo."""
    
    def __init__(self, ancho: float, alto: float):
        """Inicializa un rectángulo con ancho y alto.
        
        Args:
            ancho (float): El ancho del rectángulo
            alto (float): El alto del rectángulo
            
        Raises:
            ValueError: Si ancho o alto no son números positivos
        """
        if not isinstance(ancho, (int, float)) or ancho <= 0:
            raise ValueError("El ancho debe ser un número positivo")
        if not isinstance(alto, (int, float)) or alto <= 0:
            raise ValueError("El alto debe ser un número positivo")
            
        self._ancho = ancho
        self._alto = alto

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo.
        
        Returns:
            float: El área calculada
        """
        return self._ancho * self._alto 