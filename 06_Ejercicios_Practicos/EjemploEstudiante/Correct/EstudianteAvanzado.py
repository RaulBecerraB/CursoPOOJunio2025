from Persona import Persona

class EstudianteAvanzado(Persona):
    """
    Versión avanzada de la clase Estudiante que demuestra el uso de encapsulamiento.
    Esta clase muestra buenas prácticas de programación orientada a objetos como:
    - Encapsulamiento de atributos
    - Validación de datos
    - Uso de properties
    - Control de acceso a atributos
    """
    
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self._matricula = matricula  # Atributo "privado" con _
        self._notas = []  # Lista privada para almacenar notas
        
    @property
    def matricula(self):
        """Getter para la matrícula"""
        return self._matricula
    
    @matricula.setter
    def matricula(self, nueva_matricula):
        """Setter para la matrícula con validación"""
        if not isinstance(nueva_matricula, str):
            raise ValueError("La matrícula debe ser una cadena de texto")
        if len(nueva_matricula) < 5:
            raise ValueError("La matrícula debe tener al menos 5 caracteres")
        self._matricula = nueva_matricula
    
    def agregar_nota(self, nota):
        """Agrega una nota al estudiante con validación"""
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self._notas.append(nota)
    
    def obtener_promedio(self):
        """Calcula el promedio de las notas del estudiante"""
        if not self._notas:
            return 0
        return sum(self._notas) / len(self._notas)
    
    def decirMatricula(self):
        """Muestra la matrícula del estudiante"""
        print("Mi matricula es ", self._matricula)
        
    def estudiar(self):
        """Simula que el estudiante está estudiando"""
        print("Estoy estudiando")
        
    def __str__(self):
        """Representación en string del estudiante"""
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Matrícula: {self._matricula}, Promedio: {self.obtener_promedio():.2f}"

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un estudiante
    estudiante = EstudianteAvanzado("Juan", 20, "12345")
    
    # Agregar algunas notas
    estudiante.agregar_nota(8.5)
    estudiante.agregar_nota(9.0)
    estudiante.agregar_nota(7.5)
    
    # Mostrar información
    print(estudiante)  # Usa el método __str__
    
    # Intentar agregar una nota inválida (esto lanzará un error)
    try:
        estudiante.agregar_nota(15)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Intentar cambiar la matrícula a una inválida (esto lanzará un error)
    try:
        estudiante.matricula = "123"
    except ValueError as e:
        print(f"Error: {e}") 