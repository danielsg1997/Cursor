"""
Ejercicio de List Comprehension y Generación de Secuencias

Este módulo demuestra el uso de list comprehension en Python para generar
una lista con los cuadrados de los n primeros números naturales de forma
concisa y eficiente.

Funcionalidades:
    - Generación de lista de cuadrados usando list comprehension
    - Ejemplo práctico de sintaxis compacta de Python
    - Demostración de range() y operador de potencia

Ejemplo:
    cuadrados(10) devuelve [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

#crea una lista con los cuadrados de los n primeros numeros naturales
def cuadrados(n):
    """
    Genera una lista con los cuadrados de los n primeros números naturales.
    
    Args:
        n (int): Número de elementos a generar (desde 1 hasta n)
    
    Returns:
        list: Lista con los cuadrados de los números del 1 al n
    
    Example:
        >>> cuadrados(5)
        [1, 4, 9, 16, 25]
    """
    return [i**2 for i in range(1, n+1)]
