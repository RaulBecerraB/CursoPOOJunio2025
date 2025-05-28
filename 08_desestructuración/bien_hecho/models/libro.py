class Libro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor 

    # Getter y setter para título
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    # Getter y setter para autor
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor 