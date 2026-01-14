"""
Ejercicio de Verificación de Números Pares e Impares

Este módulo implementa una función simple para determinar si un número
ingresado por el usuario es par o impar. Utiliza el operador módulo (%)
para verificar la divisibilidad por 2.

Funcionalidades:
    - Entrada de datos del usuario mediante input()
    - Conversión de string a entero
    - Verificación de paridad usando operador módulo
    - Salida condicional basada en el resultado

Lógica:
    Un número es par si el resto de dividirlo entre 2 es 0.
    En caso contrario, el número es impar.
"""

# genera un codigo que calcule si un numero es par o impar
numero = int(input("ingrese un numero: "))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")