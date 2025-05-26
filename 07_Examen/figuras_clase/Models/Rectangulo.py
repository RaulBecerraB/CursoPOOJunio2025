from .Figura import Figura

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.set_base(base)
        self.set_altura(altura)
        
    def set_base(self, base):
        try:
            if isinstance(base, str):
                base = float(base)
        except ValueError:
            raise ValueError("La base debe ser un número")
        
        if not isinstance(base, (int, float)) or base <= 0:
            raise ValueError("La base debe ser un número positivo")
        
        self._base = base
        
    def set_altura(self, altura):
        try:
            if isinstance(altura, str):
                altura = float(altura)
        except ValueError:
            raise ValueError("La altura debe ser un número")
        
        if not isinstance(altura, (int, float)) or altura <= 0:
            raise ValueError("La altura debe ser un número positivo")
        
        self._altura = altura
    
    @property
    def base(self):
        return self._base
    
    @property
    def altura(self):
        return self._altura
        
    def calcular_area(self):
        return self.base * self.altura
