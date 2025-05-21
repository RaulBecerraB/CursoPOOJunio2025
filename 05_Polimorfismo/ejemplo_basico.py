class Animal:
    
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("El perro ladra")

class Gato(Animal):
    def hablar(self):
        print("El gato maulla")

def hazlo_hablar(animal):
    animal.hablar()  # Aquí se ve el polimorfismo

# Uso
animales = [Perro(), Gato(), Animal()]

for a in animales:
    hazlo_hablar(a)
