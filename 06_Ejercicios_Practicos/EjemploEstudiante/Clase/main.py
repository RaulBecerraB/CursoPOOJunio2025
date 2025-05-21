from Estudiante import Estudiante

# Crear un estudiante válido
estudiante = Estudiante("John", 18, "E21080774")
print("Estudiante creado exitosamente!")
estudiante.saludar()

# Intentar cambiar el nombre a un valor inválido
print("\nIntentando establecer un nombre inválido...")
try:
    estudiante.nombre = 123  # Intentando asignar un número como nombre
except ValueError as e:
    print(f"Error al cambiar el nombre: {e}")

try:
    estudiante.nombre = ""  # Intentando asignar un nombre vacío
except ValueError as e:
    print(f"Error al cambiar el nombre: {e}")

# Cambiar el nombre a un valor válido
print("\nCambiando el nombre a un valor válido...")
estudiante.nombre = "John Doe"
estudiante.saludar()

# Intentar cambiar la edad a un valor inválido
print("\nIntentando establecer una edad inválida...")
try:
    estudiante.edad = "veinte"  # Intentando asignar un string como edad
except ValueError as e:
    print(f"Error al cambiar la edad: {e}")

try:
    estudiante.edad = -5  # Intentando asignar una edad negativa
except ValueError as e:
    print(f"Error al cambiar la edad: {e}")

# Cambiar la edad a un valor válido
print("\nCambiando la edad a un valor válido...")
estudiante.edad = 20
estudiante.saludar()





