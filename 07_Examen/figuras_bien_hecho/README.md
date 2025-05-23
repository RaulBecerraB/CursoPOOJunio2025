# Calculadora de Áreas

Este proyecto implementa una calculadora de áreas para diferentes figuras geométricas (triángulos, rectángulos y círculos) utilizando principios de programación orientada a objetos.

## Estructura del Proyecto

El código está organizado siguiendo el principio de responsabilidad única, con cada clase en su propio archivo:

- `figura.py`: Define la clase abstracta base `Figura`
- `triangulo.py`: Implementa la clase `Triangulo`
- `rectangulo.py`: Implementa la clase `Rectangulo`
- `circulo.py`: Implementa la clase `Circulo`
- `calculadora_areas.py`: Gestiona la interacción con el usuario
- `main.py`: Punto de entrada de la aplicación

## Principios de POO Aplicados

- **Encapsulación**: Atributos protegidos con prefijo `_`
- **Herencia**: Las figuras heredan de la clase base abstracta `Figura`
- **Polimorfismo**: El método `calcular_area()` se implementa en cada subclase
- **Abstracción**: `Figura` define una interfaz abstracta para todas las figuras
- **Responsabilidad Única**: Separación de lógica de negocio e interfaz de usuario

## Ejecutar el Programa

```bash
python main.py
```
