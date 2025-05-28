from Models.Libro import Libro

class Biblioteca: 
    def __init__(self,nombre):
        self._nombre = nombre
        
    _libros = []
    
    @property
    def libros(self):
        return self._libros
            
    def agregar_libro(self,libro):
        if isinstance(libro, Libro):
            self._libros.append(libro)
        else:
            print("El objeto no es un libro")