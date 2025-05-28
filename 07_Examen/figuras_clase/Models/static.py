from Triangulo import Triangulo

# Crear una instancia de Triangulo
triangulo = Triangulo(10, 5)
area_instancia = triangulo.calcular_area()
print(f"Área calculada con instancia: {area_instancia}")

# Llamar al método estático directamente desde la clase
area_estatica = Triangulo.calcular_area(10, 5)
print(f"Área calculada con método estático: {area_estatica}")

