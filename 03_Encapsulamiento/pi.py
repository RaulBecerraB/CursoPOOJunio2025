class Calculadora:
    def __init__(self):
        self.__pi = 3.14159

    def calcular_area_circulo(self, radio):
        return self.__pi * radio ** 2
    
    def obtener_pi(self):
        return self.__pi

calculadora = Calculadora()
print(calculadora.calcular_area_circulo(6))
print(calculadora.obtener_pi())
