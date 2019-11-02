"""Crie um programa que leia dois números e mostre a soma entre eles."""

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
somador = numero2 + numero1

def soma(numero1, numero2):
    print('{} + {} = {}'.format(numero1, numero2, somador))
    return somador

soma(numero1, numero2)