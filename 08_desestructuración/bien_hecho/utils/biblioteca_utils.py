from models.libro import Libro

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== MENÚ BIBLIOTECA ===")
    print("1. Ver todos los libros")
    print("2. Agregar nuevo libro")
    print("3. Buscar por autor")
    print("4. Buscar por título")
    print("5. Salir")
    return input("\nSeleccione una opción (1-5): ")

def ver_libros(biblioteca):
    """Muestra todos los libros de la biblioteca"""
    print(f"\nBiblioteca: {biblioteca.nombre}")
    if not biblioteca.libros:
        print("No hay libros en la biblioteca.")
        return
        
    for libro in biblioteca.libros:
        print(f"  • '{libro.titulo}' por {libro.autor}")

def agregar_libro(biblioteca):
    """Permite al usuario agregar un nuevo libro"""
    print("\n=== AGREGAR NUEVO LIBRO ===")
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    
    if not titulo or not autor:
        print("El título y el autor son obligatorios.")
        return
        
    nuevo_libro = Libro(titulo, autor)
    biblioteca.agregar_libro(nuevo_libro)
    print(f"Libro '{titulo}' agregado correctamente.")

def buscar_por_autor(biblioteca, buscador):
    """Permite al usuario buscar libros por autor"""
    print("\n=== BUSCAR POR AUTOR ===")
    autor = input("Ingrese el nombre del autor: ")
    
    if not autor:
        print("Debe ingresar un nombre de autor.")
        return
        
    buscador.buscar_por_autor(biblioteca, autor)
    print(buscador.mostrar_resultados())

def buscar_por_titulo(biblioteca):
    """Permite al usuario buscar libros por título"""
    print("\n=== BUSCAR POR TÍTULO ===")
    titulo = input("Ingrese el título o parte del título: ")
    
    if not titulo:
        print("Debe ingresar un título para buscar.")
        return
        
    resultados = []
    for libro in biblioteca.libros:
        if titulo.lower() in libro.titulo.lower():
            resultados.append(libro)
            
    if not resultados:
        print("No se encontraron libros con ese título.")
    else:
        print("Resultados encontrados:")
        for libro in resultados:
            print(f"  • '{libro.titulo}' por {libro.autor}")

def cargar_libros_ejemplo(biblioteca):
    """Carga algunos libros de ejemplo en la biblioteca"""
    biblioteca.agregar_libro(Libro("Clean Code", "Robert C. Martin"))
    biblioteca.agregar_libro(Libro("La casa de los espíritus", "Isabel Allende"))
    biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez")) 