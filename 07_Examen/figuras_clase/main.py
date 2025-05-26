from Models.Rectangulo import Rectangulo
from Models.Triangulo import Triangulo
from Models.Circulo import Circulo

def main():
    print("=== Calculadora de Áreas ===")
    print("1) Rectángulo")
    print("2) Triangulo")
    print("3) Circulo")
    
    try:
        opcion = int(input("Selecciona una figura:"))
        # Calcular rectangulo
        if opcion == 1:
            try:
                base = input("Ingresa la base:")
                altura = input("Ingresa la altura:")
                rectangulo = Rectangulo(base, altura)
                print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
            except ValueError as e:
                print(f"Error: {e}")
        # Calcular triangulo
        elif opcion == 2:
            try:
                base = input("Ingresa la base:")
                altura = input("Ingresa la altura:")
                triangulo = Triangulo(base, altura)
                print(f"El área del triangulo es: {triangulo.calcular_area()}")
            except ValueError as e:
                print(f"Error: {e}")
        # Calcular circulo
        elif opcion == 3:
            try:
                radio = input("Ingresa el radio:")
                circulo = Circulo(radio)
                print(f"El área del Circulo es: {circulo.calcular_area()}")
            except ValueError as e:
                print(f"Error: {e}")
        
        else:
            print("Opcion no valida")
    except ValueError:
        print("Error: Debes ingresar un número para seleccionar la opción")

if __name__ == "__main__":
    main()