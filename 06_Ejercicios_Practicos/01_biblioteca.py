"""
Ejercicio práctico: Sistema de Biblioteca
Este ejercicio combina todos los conceptos de POO:
- Clases y Objetos
- Encapsulamiento
- Herencia
- Polimorfismo
"""

class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True
    
    def obtener_titulo(self):
        return self._titulo
    
    def obtener_autor(self):
        return self._autor
    
    def obtener_isbn(self):
        return self._isbn
    
    def esta_disponible(self):
        return self._disponible
    
    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False
    
    def devolver(self):
        self._disponible = True
    
    def mostrar_info(self):
        print(f"\nInformación del libro:")
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"ISBN: {self._isbn}")
        print(f"Estado: {'Disponible' if self._disponible else 'Prestado'}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato):
        super().__init__(titulo, autor, isbn)
        self._formato = formato
        self._descargas = 0
    
    def descargar(self):
        self._descargas += 1
        print(f"Libro descargado. Total de descargas: {self._descargas}")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Formato: {self._formato}")
        print(f"Descargas: {self._descargas}")

class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id = id_usuario
        self._libros_prestados = []
    
    def prestar_libro(self, libro):
        if libro.prestar():
            self._libros_prestados.append(libro)
            print(f"{self._nombre} ha prestado el libro: {libro.obtener_titulo()}")
            return True
        print(f"El libro {libro.obtener_titulo()} no está disponible")
        return False
    
    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()
            self._libros_prestados.remove(libro)
            print(f"{self._nombre} ha devuelto el libro: {libro.obtener_titulo()}")
            return True
        print(f"{self._nombre} no tiene prestado el libro: {libro.obtener_titulo()}")
        return False
    
    def mostrar_libros_prestados(self):
        print(f"\nLibros prestados a {self._nombre}:")
        if not self._libros_prestados:
            print("No tiene libros prestados")
        else:
            for libro in self._libros_prestados:
                print(f"- {libro.obtener_titulo()}")

# Creando algunos libros
libro1 = Libro("Python para Principiantes", "Juan Pérez", "123-456")
libro2 = LibroDigital("Python Avanzado", "María García", "789-012", "PDF")

# Creando usuarios
usuario1 = Usuario("Ana", "001")
usuario2 = Usuario("Carlos", "002")

# Probando el sistema
print("Probando el sistema de biblioteca:")

# Mostrar información de los libros
libro1.mostrar_info()
libro2.mostrar_info()

# Prestar libros
usuario1.prestar_libro(libro1)
usuario2.prestar_libro(libro2)

# Intentar prestar un libro ya prestado
usuario2.prestar_libro(libro1)

# Mostrar libros prestados
usuario1.mostrar_libros_prestados()
usuario2.mostrar_libros_prestados()

# Devolver libros
usuario1.devolver_libro(libro1)
usuario2.devolver_libro(libro2)

# Descargar libro digital
libro2.descargar()
libro2.descargar()

# Mostrar estado final
print("\nEstado final de los libros:")
libro1.mostrar_info()
libro2.mostrar_info() 