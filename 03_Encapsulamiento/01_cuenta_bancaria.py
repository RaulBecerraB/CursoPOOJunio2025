"""
Ejemplo de una clase CuentaBancaria
Este ejemplo muestra el concepto de encapsulamiento en Python
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos privados (convención en Python usando _)
        self._titular = titular
        self._saldo = saldo_inicial
        self._movimientos = []
    
    # Getters (métodos para obtener valores)
    def obtener_titular(self):
        return self._titular
    
    def obtener_saldo(self):
        return self._saldo
    
    def obtener_movimientos(self):
        return self._movimientos.copy()  # Retornamos una copia para proteger los datos
    
    # Setters (métodos para modificar valores)
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            self._movimientos.append(f"Depósito: +{cantidad}")
            print(f"Depósito exitoso. Saldo actual: {self._saldo}")
        else:
            print("Error: La cantidad debe ser positiva")
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self._saldo:
                self._saldo -= cantidad
                self._movimientos.append(f"Retiro: -{cantidad}")
                print(f"Retiro exitoso. Saldo actual: {self._saldo}")
            else:
                print("Error: Saldo insuficiente")
        else:
            print("Error: La cantidad debe ser positiva")
    
    def mostrar_info(self):
        print(f"\nInformación de la cuenta:")
        print(f"Titular: {self._titular}")
        print(f"Saldo actual: {self._saldo}")
        print("\nÚltimos movimientos:")
        for movimiento in self._movimientos[-5:]:  # Mostrar solo los últimos 5 movimientos
            print(movimiento)

# Creando una cuenta bancaria
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

# Probando los métodos
print("Probando la cuenta bancaria:")
mi_cuenta.mostrar_info()

mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.depositar(1000)
mi_cuenta.retirar(300)

mi_cuenta.mostrar_info()

# Intentando acceder directamente a los atributos privados
print("\nIntentando acceder a los atributos privados:")
print(f"Titular (usando getter): {mi_cuenta.obtener_titular()}")
print(f"Saldo (usando getter): {mi_cuenta.obtener_saldo()}")

# Nota: En Python, los atributos privados son más una convención que una restricción real
# Los estudiantes deben entender que el prefijo _ indica "no acceder directamente" 