from .figura import Figura

class Triangulo(Figura):
    """Clase que representa un triángulo."""
    
    def __init__(self, base: float, altura: float):
        """Inicializa un triángulo con base y altura.
        
        Args:
            base (float): La base del triángulo
            altura (float): La altura del triángulo
        """
        self._base = base
        self._altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del triángulo.
        
        Returns:
            float: El área calculada
        """
        return 0.5 * self._base * self._altura 