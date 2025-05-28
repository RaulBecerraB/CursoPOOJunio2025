from Models.Libro import Libro
from Models.Biblioteca import Biblioteca

#Libros
libro = Libro("El señor de los anillos","J.R.R. Tolkien")
libro2 = Libro("Clean Code","Robert C.Martin")

#Biblioteca
biblioteca = Biblioteca("Mi biblioteca")

#Agregar Libros
biblioteca.agregar_libro(libro)
biblioteca.agregar_libro(libro2)

#Mostrar libros
for libro in biblioteca.libros:
    print(libro.titulo, libro.autor)

