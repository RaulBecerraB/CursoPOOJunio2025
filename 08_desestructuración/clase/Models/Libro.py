class Libro:
    def __init__(self,titulo,autor):
        self._titulo = titulo
        self._autor = autor
        
    #Getters y setters para titulo y autor
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter    
    def titulo(self,valor):
        self._titulo = valor
        
    #Getters y setters para titulo y autor
    @property
    def autor(self):
        return self._autor
    
    @autor.setter    
    def autor(self,valor):
        self._autor = valor
        