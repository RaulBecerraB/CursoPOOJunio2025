from models.biblioteca import Biblioteca
from models.buscador import Buscador
from utils.biblioteca_utils import (
    mostrar_menu,
    ver_libros,
    agregar_libro,
    buscar_por_autor,
    buscar_por_titulo,
    cargar_libros_ejemplo
)

def main():
    biblioteca = Biblioteca("Biblioteca Central")
    buscador = Buscador()
    
    cargar_libros_ejemplo(biblioteca)
    
    print(f"\nBienvenido a {biblioteca.nombre}!")
    
    # Bucle principal del programa
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            ver_libros(biblioteca)
        elif opcion == "2":
            agregar_libro(biblioteca)
        elif opcion == "3":
            buscar_por_autor(biblioteca, buscador)
        elif opcion == "4":
            buscar_por_titulo(biblioteca)
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema de biblioteca!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()