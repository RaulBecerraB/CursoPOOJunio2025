from .Figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.set_base(base)
        self.set_altura(altura)
        
    def set_base(self, base):
        # Validamos que sea un número positivo
        if not isinstance(base, (int, float)) or base <= 0:
            raise ValueError("La base debe ser un número positivo")
            
        self._base = base
        
    def set_altura(self, altura):     
        # Validamos que sea un número positivo
        if not isinstance(altura, (int, float)) or altura <= 0:
            raise ValueError("La altura debe ser un número positivo")
            
        self._altura = altura
        
    @property
    def base(self):
        """Getter para la base del triángulo."""
        return self._base
        
    @property
    def altura(self):
        """Getter para la altura del triángulo."""
        return self._altura
        
    def calcular_area(self):
        return (self._base * self._altura) / 2
