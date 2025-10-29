"""Generador de contraseñas aleatorias (sin control de errores).

Versión simplificada: no realiza validaciones ni captura excepciones. Convierte
la entrada a entero directamente y genera la contraseña con los conjuntos de
caracteres seleccionados.
"""

import secrets
import string


def generar_contrasena(n, usar_mayus=True, usar_minus=True, usar_digitos=True, usar_simbolos=True):
    """Genera y devuelve una contraseña aleatoria de longitud n.

    Nota: esta versión no realiza validaciones ni capturas de error.
    """
    longitud = int(n)

    caracteres = ''
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    return ''.join(secrets.choice(caracteres) for _ in range(longitud))


if __name__ == "__main__":
    entrada = input("Ingrese la longitud deseada de la contraseña (entero positivo): ")
    n = int(entrada)
    pwd = generar_contrasena(n)
    print("Contraseña generada:", pwd)

