class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados = []
        
    # Getters y setters
    @property
    def nombre(self):
        return self._nombre
        
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def libros_prestados(self):
        return self._libros_prestados
    
    # Métodos para interactuar con la biblioteca
    def pedir_prestado(self, biblioteca, titulo_libro):
        """Pide prestado un libro de la biblioteca por su título"""
        for libro in biblioteca.libros:
            if libro.titulo == titulo_libro and libro not in self._libros_prestados:
                self._libros_prestados.append(libro)
                return True
        return False
    
    def devolver_libro(self, titulo_libro):
        """Devuelve un libro que el usuario tenía prestado"""
        for libro in self._libros_prestados:
            if libro.titulo == titulo_libro:
                self._libros_prestados.remove(libro)
                return True
        return False
    
    def listar_libros_prestados(self):
        """Muestra los libros que tiene prestados el usuario"""
        if not self._libros_prestados:
            return "No tiene libros prestados actualmente."
        
        resultado = f"Libros prestados a {self._nombre}:"
        for libro in self._libros_prestados:
            resultado += f"\n  • '{libro.titulo}' por {libro.autor}"
        return resultado 