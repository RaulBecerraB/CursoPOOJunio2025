from models.libro import Libro

class Biblioteca:
    def __init__(self, nombre, libros=None):
        self._nombre = nombre
        self._libros = libros or []  # Composición: Biblioteca contiene una lista de Libros

    # Getter y setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # Getter para la lista de libros
    @property
    def libros(self):
        return self._libros

    # Método para agregar libros
    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self._libros.append(libro)
        else:
            raise TypeError("Debe proporcionar un objeto Libro") 