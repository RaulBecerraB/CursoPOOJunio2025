class Buscador:
    def __init__(self):
        self._ultimo_resultado = None
    
    @property
    def ultimo_resultado(self):
        return self._ultimo_resultado
    
    def buscar_por_autor(self, biblioteca, nombre_autor):
        """Busca libros de un autor específico en la biblioteca"""
        resultado = []
        for libro in biblioteca.libros:
            if nombre_autor.lower() in libro.autor.lower():
                resultado.append(libro)
        
        self._ultimo_resultado = resultado
        return resultado
    
    def mostrar_resultados(self):
        """Muestra los resultados de la última búsqueda"""
        if not self._ultimo_resultado:
            return "No hay resultados de búsqueda."
        
        texto = "Resultados encontrados:"
        for libro in self._ultimo_resultado:
            texto += f"\n  • '{libro.titulo}' por {libro.autor}"
        return texto 