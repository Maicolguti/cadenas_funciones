# -*- coding: utf-8 -*-
"""
Programa: Contador de vocales, consonantes y espacios
Descripción:
    Este programa solicita al usuario una cadena de texto y muestra:
    - El número total de caracteres.
    - El número total de vocales.
    - El número total de consonantes.
    - El número de espacios.
"""

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador


def contar_consonantes(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter.isalpha() and caracter not in vocales:
            contador += 1
    return contador


def contar_espacios(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isspace():
            contador += 1
    return contador


def contar_caracteres_totales(cadena):
    contador = 0
    for caracter in cadena:
        contador += 1
    return contador


# ====================== PROGRAMA PRINCIPAL ======================

texto = input("Ingrese una cadena de texto: ")

total_caracteres = contar_caracteres_totales(texto)
total_vocales = contar_vocales(texto)
total_consonantes = contar_consonantes(texto)
total_espacios = contar_espacios(texto)

print("Número total de caracteres:", total_caracteres)
print("Número de vocales:", total_vocales)
print("Número de consonantes:", total_consonantes)
print("Número de espacios:", total_espacios)
