"""
Ejercicio de FizzBuzz

Este módulo implementa el clásico juego de programación FizzBuzz, que imprime
números del 1 al 50 con las siguientes reglas:
    - Si el número es divisible por 3: imprime "Fizz"
    - Si el número es divisible por 5: imprime "Buzz"
    - Si el número es divisible por ambos (3 y 5): imprime "FizzBuzz"
    - En caso contrario: imprime el número

Funcionalidades:
    - Iteración sobre un rango de números (1 a 50)
    - Uso de operador módulo (%) para verificar divisibilidad
    - Estructuras condicionales anidadas (if-elif-else)
    - Ejercicio clásico de programación para practicar lógica condicional

Este es un ejercicio muy común en entrevistas técnicas y ayuda a practicar
el pensamiento lógico y el manejo de condiciones múltiples.
"""

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)