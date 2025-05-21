class Forma:
    def area(self):
        pass
    
    def imprimir_area(self):
        print(f"Area: {self.area()}")

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

formas = [Circulo(5), Rectangulo(4, 6)]

for f in formas:
    f.imprimir_area()
