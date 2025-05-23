from Models.figura import Figura
from Models.triangulo import Triangulo
from Models.rectangulo import Rectangulo
from Models.circulo import Circulo

class CalculadoraAreas:
    """Clase responsable de la interacción con el usuario y control de flujo."""
    
    def ejecutar(self):
        """Ejecuta la calculadora de áreas, interactuando con el usuario."""
        print("=== Calculadora de Áreas ===")
        print("1) Triángulo\n2) Rectángulo\n3) Círculo")
        opcion = input("Seleccione una figura (1/2/3): ").strip()

        try:
            if opcion == "1":
                base = float(input("📐 Ingrese la base del triángulo: "))
                altura = float(input("📏 Ingrese la altura del triángulo: "))
                figura: Figura = Triangulo(base, altura)

            elif opcion == "2":
                ancho = float(input("📐 Ingrese el ancho del rectángulo: "))
                alto = float(input("📏 Ingrese el alto del rectángulo: "))
                figura: Figura = Rectangulo(ancho, alto)

            elif opcion == "3":
                radio = float(input("🔵 Ingrese el radio del círculo: "))
                figura: Figura = Circulo(radio)

            else:
                raise ValueError("Opción inválida.")

            area = figura.calcular_area()   # Polimorfismo: invocamos el mismo método en diferentes clases
            print(f"\n✔ El área calculada es: {area:.2f}")

        except ValueError as e:
            print(f"\n❌ Error: {e}") 