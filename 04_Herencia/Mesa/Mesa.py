class Mesa:
    def __init__(self,color,material,tamaño,num_patas):
        self.color = color
        self.material = material
        self.tamaño = tamaño
        self.num_patas = num_patas
        
    palabra = "Hola"
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, nuevo_color):
        if not isinstance(nuevo_color, str):
            raise TypeError("El color debe ser una cadena de texto (string)")
        self._color = nuevo_color
