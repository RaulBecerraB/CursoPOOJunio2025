"""
Ejemplo de polimorfismo usando formas geométricas
Este ejemplo muestra cómo diferentes clases pueden implementar los mismos métodos
de manera diferente, pero ser tratadas de forma uniforme
"""

from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass
    
    def mostrar_info(self):
        print(f"\nInformación de la {self.nombre}:")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, lado2, lado3):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.base + self.lado2 + self.lado3

# Creando objetos de diferentes formas
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 4, 5, 5)

# Demostrando polimorfismo
print("Demostrando polimorfismo con formas geométricas:")

# Podemos tratar todas las formas de manera uniforme
formas = [circulo, rectangulo, triangulo]

# Calcular y mostrar información de todas las formas
for forma in formas:
    forma.mostrar_info()

# Ejemplo de polimorfismo en acción
print("\nCalculando el área total de todas las formas:")
area_total = sum(forma.calcular_area() for forma in formas)
print(f"Área total: {area_total:.2f}")

# Ejemplo de polimorfismo con un método específico
print("\nVerificando si las formas son grandes (área > 50):")
for forma in formas:
    es_grande = "sí" if forma.calcular_area() > 50 else "no"
    print(f"¿{forma.nombre} es grande? {es_grande}")

# Notas importantes sobre el polimorfismo:
# 1. Todas las formas implementan los mismos métodos (calcular_area y calcular_perimetro)
# 2. Cada forma implementa estos métodos de manera diferente
# 3. Podemos tratar todas las formas de manera uniforme
# 4. El código que usa estas formas no necesita saber qué tipo específico de forma es 