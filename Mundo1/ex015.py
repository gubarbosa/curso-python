"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira."""
#from math import trunc

numero_real = float(input('Número real qualquer: '))

def porcaoInteira(numero_real):
    parte_inteira = numero_real       #math.trunc(numero_real)  #int(numero_real)
    print('A parte inteira de {} é {:.0f}'.format(numero_real, parte_inteira))
    return parte_inteira

porcaoInteira(numero_real)