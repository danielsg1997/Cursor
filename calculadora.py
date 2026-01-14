def calculadora(a, b, operacion):
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
