from .Figura import Figura

class Circulo(Figura):
    def __init__(self, radio):
        self.set_radio(radio)
        
    def set_radio(self, radio):
        try:
            if isinstance(radio, str):
                radio = float(radio)
        except ValueError:
            raise ValueError("El radio debe ser un número")
        
        if not isinstance(radio, (int, float)) or radio <= 0:
            raise ValueError("El radio debe ser un número positivo")
        
        self._radio = radio
        
    @property
    def radio(self):
        return self._radio
    
    def calcular_area(self):
        return 3.14 * self.radio ** 2