"""Comprobador de palíndromos.

Este módulo contiene la función `es_palindromo` que verifica si una cadena es
palíndroma ignorando espacios, signos de puntuación y diferencia entre
mayúsculas/minúsculas. Incluye un bloque ejecutable para usarlo desde la
línea de comandos.
"""

def es_palindromo(cadena):
    """Comprueba si una cadena es un palíndromo.

    Procedimiento:
    1) Elimina todos los caracteres que no sean alfanuméricos (letras o dígitos).
    2) Convierte el resultado a minúsculas.
    3) Compara la cadena "limpia" con su reverso. Si son iguales, es palíndromo.

    Parámetros:
    cadena (str): Texto de entrada que puede contener espacios, signos de puntuación, etc.

    Retorna:
    bool: True si la cadena (ignorando puntuación y mayúsculas/minúsculas) es palíndroma, False en caso contrario.
    """
    # Construir cadena limpia con solo caracteres alfanuméricos y en minúsculas
    cadena_limpia = ''.join(c for c in cadena if c.isalnum()).lower()

    # Comparar con su reverso
    return cadena_limpia == cadena_limpia[::-1]


if __name__ == "__main__":
    texto = input("Ingrese una cadena de texto: ")
    if es_palindromo(texto):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")
