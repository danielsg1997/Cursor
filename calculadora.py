"""
Ejercicio de Calculadora Interactiva

Este módulo implementa una calculadora básica interactiva que permite realizar
operaciones aritméticas fundamentales (suma, resta, multiplicación, división)
mediante un bucle interactivo que continúa hasta que el usuario decide salir.

Funcionalidades:
    - Operaciones soportadas: suma (+), resta (-), multiplicación (*), división (/)
    - Manejo de errores para división por cero
    - Interfaz interactiva mediante entrada por consola
    - Bucle continuo hasta que el usuario escriba "salir"

Uso:
    El programa solicita dos números y una operación en cada iteración.
    Para terminar, escribir "salir" cuando se solicite la operación.
"""

def calculadora(a, b, operacion):
    """
    Realiza una operación aritmética básica entre dos números.
    
    Args:
        a (int): Primer número para la operación
        b (int): Segundo número para la operación
        operacion (str): Operación a realizar. Debe ser uno de: '+', '-', '*', '/'
    
    Returns:
        float: Resultado de la operación aritmética
    
    Raises:
        ZeroDivisionError: Si se intenta dividir entre cero
    """
    #realizar la operacion
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b

# Bucle principal que se repite hasta que el usuario escriba "salir"
while True:
    #pedir al usuario dos numeros y una operacion
    a = int(input("ingrese el primer numero: "))
    b = int(input("ingrese el segundo numero: "))
    operacion = input("ingrese la operacion (o 'salir' para terminar): ")
    
    # Si el usuario escribe "salir", terminar el bucle
    if operacion.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    # Ejecutar la operacion y mostrar el resultado
    try:
        resultado = calculadora(a, b, operacion)
        print(f"el resultado de la operacion es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero. Por favor, intenta con otro número.")
    print()  # Línea en blanco para mejor legibilidad
