"""
Ejemplo de transición de arreglos a objetos
Este ejemplo muestra cómo podemos pasar de usar arreglos a usar objetos
para representar la información de estudiantes
"""

# Usando arreglos
nombres = ["Juan", "María", "Pedro"]
edades = [20, 19, 21]
notas = [8.5, 9.0, 7.5]

# Accediendo a la información de un estudiante
print("Usando arreglos:")
print(f"Nombre: {nombres[0]}")
print(f"Edad: {edades[0]}")
print(f"Nota: {notas[0]}")
print("\n" + "-"*50 + "\n")

# Usando una clase (introducción a POO)
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota: {self.nota}")

# Creando objetos de tipo Estudiante
estudiante1 = Estudiante("Juan", 20, 8.5)
estudiante2 = Estudiante("María", 19, 9.0)
estudiante3 = Estudiante("Pedro", 21, 7.5)

# Accediendo a la información de un estudiante usando objetos
print("Usando objetos:")
estudiante1.mostrar_info()

# Ventajas de usar objetos:
# 1. La información está agrupada lógicamente
# 2. Es más fácil de mantener y entender
# 3. Podemos agregar comportamiento (métodos) a nuestros datos 