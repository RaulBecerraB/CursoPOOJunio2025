"""
Ejemplo de herencia usando una jerarquía de animales
Este ejemplo muestra el concepto de herencia en Python
"""

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        print("El animal hace un sonido")
    
    def mostrar_info(self):
        print(f"\nInformación del animal:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        
        

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_sonido(self):
        print("¡Guau! ¡Guau!")
    
    def mostrar_info(self):
        # Llamar al método de la clase padre
        super().mostrar_info()
        print(f"Raza: {self.raza}")
    
    def buscar_pelota(self):
        print(f"{self.nombre} está buscando la pelota")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def hacer_sonido(self):
        print("¡Miau! ¡Miau!")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")
    
    def trepar_arbol(self):
        print(f"{self.nombre} está trepando un árbol")

# Creando objetos
mi_perro = Perro("Rex", 3, "Labrador")
mi_gato = Gato("Mittens", 2, "Naranja")

# Probando los métodos
print("Probando el perro:")
mi_perro.mostrar_info()
mi_perro.hacer_sonido()
mi_perro.buscar_pelota()

print("\nProbando el gato:")
mi_gato.mostrar_info()
mi_gato.hacer_sonido()
mi_gato.trepar_arbol()

# Demostrando polimorfismo
print("\nDemostrando polimorfismo:")
animales = [mi_perro, mi_gato]
for animal in animales:
    print(f"\n{animal.nombre} dice:")
    animal.hacer_sonido() 