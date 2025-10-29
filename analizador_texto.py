"""Analizador de texto sencillo: cuenta palabras, frases y párrafos.

Implementación simple y legible. Las funciones usan split y operaciones
básicas para facilitar la comprensión.
"""

import re
import sys


def contar_palabras(texto):
    """Cuenta palabras usando split por espacios.

    Devuelve 0 si el texto está vacío o solo contiene espacios.
    """
    if not texto or not texto.strip():
        return 0
    return len(texto.split())


def contar_frases(texto):
    """Cuenta frases separando por los caracteres . ! ?.

    Realiza una división simple y cuenta las partes no vacías.
    """
    if not texto or not texto.strip():
        return 0
    partes = re.split(r'[.!?]+', texto)
    partes = [p for p in partes if p.strip()]
    return len(partes)


def contar_parrafos(texto):
    """Cuenta párrafos separando por doble salto de línea ('\n\n').

    Trata múltiples saltos seguidos como un solo separador.
    """
    if not texto or not texto.strip():
        return 0
    partes = [p for p in texto.split('\n\n') if p.strip()]
    return len(partes)


def resumen_texto(texto):
    """Devuelve un diccionario con los conteos: palabras, frases y párrafos."""
    return {
        'palabras': contar_palabras(texto),
        'frases': contar_frases(texto),
        'parrafos': contar_parrafos(texto),
    }


if __name__ == "__main__":
    print("Pegue o escriba el texto y presione Ctrl+Z (Windows) o Ctrl+D (Unix) luego Enter para finalizar:")
    texto = sys.stdin.read()
    r = resumen_texto(texto)
    print("Palabras:", r['palabras'])
    print("Frases:", r['frases'])
    print("Párrafos:", r['parrafos'])
