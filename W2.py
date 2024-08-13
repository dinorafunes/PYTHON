#Dinora Verenice Funes Lemus (Función input)

def imprimir_numero():
    try:
        number = int(input('Por favor ingrese un número: '))
        print(f"El número ingresado es: {number}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

imprimir_numero()