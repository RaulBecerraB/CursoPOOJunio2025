"""
Ejemplo de una clase Automovil
Este ejemplo muestra los conceptos básicos de clases y objetos en Python
"""

class Automovil:
    # Constructor de la clase
    def __init__(self, marca, modelo, color):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        self.encendido = False
    
    # Métodos de la clase
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} se ha encendido")
        else:
            print("El auto ya está encendido")
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print(f"El {self.marca} {self.modelo} se ha apagado")
        else:
            print("El auto ya está apagado")
    
    def acelerar(self, cantidad):
        if self.encendido:
            self.velocidad += cantidad
            print(f"Velocidad actual: {self.velocidad} km/h")
        else:
            print("El auto está apagado")
    
    def frenar(self, cantidad):
        if self.encendido:
            self.velocidad = max(0, self.velocidad - cantidad)
            print(f"Velocidad actual: {self.velocidad} km/h")
        else:
            print("El auto está apagado")
    
    def mostrar_info(self):
        print(f"\nInformación del automóvil:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Estado: {'Encendido' if self.encendido else 'Apagado'}")

# Creando objetos de tipo Automovil
mi_auto = Automovil("Toyota", "Corolla", "Rojo")
auto_vecino = Automovil("Honda", "Civic", "Azul")

# Probando los métodos
print("Probando mi auto:")
mi_auto.mostrar_info()
mi_auto.encender()
mi_auto.acelerar(50)
mi_auto.frenar(20)
mi_auto.mostrar_info()
mi_auto.apagar()

print("\nProbando el auto del vecino:")
auto_vecino.mostrar_info()
auto_vecino.encender()
auto_vecino.acelerar(30)
auto_vecino.mostrar_info() 