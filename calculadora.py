#funciones


"""Calculadora simple con operaciones básicas.

Funciones:
- sumar(a, b): devuelve la suma de a y b.
- restar(a, b): devuelve la resta a - b.
- multiplicar(a, b): devuelve el producto a * b.
- dividir(a, b): devuelve a / b o un mensaje de error si b es 0.

Nota: la parte de entrada/salida está protegida por
`if __name__ == "__main__"` para permitir la importación del módulo
sin ejecutar la interacción con el usuario.
"""

def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta a - b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto a * b."""
    return a * b


def dividir(a, b):
    """Devuelve la división a / b o una cadena de error si b == 0."""
    if b == 0:
        return "Error: División por cero"
    return a / b



    # Leer dos números desde la entrada (se convierten a float)
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

    # Leer la operación a realizar
operacion = input("Ingrese la operación (+, -, *, /): ")

    # Seleccionar la función adecuada según la operación
if operacion == "+":
    resultado = sumar(num1, num2)
elif operacion == "-":
    resultado = restar(num1, num2)
elif operacion == "*":
    resultado = multiplicar(num1, num2)
elif operacion == "/":
    resultado = dividir(num1, num2)
else:
    resultado = "Operación no válida"

    # Mostrar el resultado
print("Resultado:", resultado)