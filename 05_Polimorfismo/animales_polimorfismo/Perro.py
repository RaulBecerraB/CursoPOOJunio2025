from Animal import Animal

class Perro(Animal):
    def __init__(self,nombre, edad, color):
        super().__init__(nombre, edad, color)
        
    def hacer_sonido(self):
        print("Guau")