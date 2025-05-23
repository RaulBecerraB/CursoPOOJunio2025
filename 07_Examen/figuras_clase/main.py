from Models.Rectangulo import Rectangulo
from Models.Triangulo import Triangulo
from Models.Circulo import Circulo

def main():
    print("=== Calculadora de Áreas ===")
    print("1) Rectángulo")
    print("2) Triangulo")
    print("3) Circulo")
    
    opcion = int(input("Selecciona una figura:"))
    
    # Calcular rectangulo
    if opcion == 1:
        base = float(input("Ingresa la base:"))
        altura = float(input("Ingresa la altura:"))
        
        rectangulo = Rectangulo(base, altura)
        print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        
    # Calcular triangulo
    elif opcion == 2:
        base = float(input("Ingresa la base:"))
        altura = float(input("Ingresa la altura:"))
        
        triangulo = Triangulo(base, altura)
        print(f"El área del triangulo es: {triangulo.calcular_area()}")
    
    # Calcular circulo
    elif opcion == 3:
        radio = float(input("Ingresa el radio:"))
        circulo = Circulo(radio)
        print(f"El área del Circulo es: {circulo.calcular_area()}")
    
    else:
        print("Opcion no valida")

if __name__ == "__main__":
    main()