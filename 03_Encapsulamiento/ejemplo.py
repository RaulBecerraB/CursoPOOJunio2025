class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre      # Atributo "protegido"
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero no negativo")


# Uso
persona = Persona("Ana", 30)
print(persona.nombre)  # Ana
persona.nombre = "Carlos"
print(persona.nombre)  # Carlos

persona.edad = 35
print(persona.edad)    # 35
