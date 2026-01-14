import math


def es_primo(n):
    """
    Verifica si un número es primo.
    
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.
    
    Args:
        n (int): El número a verificar
        
    Returns:
        bool: True si el número es primo, False en caso contrario
    """
    # Los números menores a 2 no son primos
    if n < 2:
        return False
    
    # El 2 es el único número par primo
    if n == 2:
        return True
    
    # Cualquier número par mayor que 2 no es primo
    if n % 2 == 0:
        return False
    
    # Solo necesitamos verificar divisores impares hasta la raíz cuadrada de n
    # Si n tiene un divisor mayor que sqrt(n), también tiene uno menor que sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Solicitar un número al usuario
try:
    numero = int(input("Introduce un número para verificar si es primo: "))
    
    if es_primo(numero):
        print(f"\nEl número {numero} ES primo.")
    else:
        print(f"\nEl número {numero} NO es primo.")
except ValueError:
    print("\nError: Por favor, introduce un número entero válido.")
except Exception as e:
    print(f"\nError: {e}")
