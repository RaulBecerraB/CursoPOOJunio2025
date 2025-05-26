from .figura import Figura

class Triangulo(Figura):
    """Clase que representa un triángulo."""
    
    def __init__(self, base: float, altura: float):
        if not self.esNumeroPositivo(base):
            raise ValueError("La base debe ser un número positivo")
        if not self.esNumeroPositivo(altura):
            raise ValueError("La altura debe ser un número positivo")
            
        self._base = base
        self._altura = altura
        
    def esNumeroPositivo(self, valor: float) -> bool:
        return isinstance(valor, (int, float)) and valor > 0

    def calcular_area(self) -> float:
        """Calcula el área del triángulo.
        
        Returns:
            float: El área calculada
        """
        return 0.5 * self._base * self._altura 