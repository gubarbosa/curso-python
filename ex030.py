"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""
numero_int = int(input('Número inteiro: '))

def parImpar(numero_int):
    if numero_int % 2 == 0:
        print('O numero {} é par'.format(numero_int))
    else:
        print('O número {} é ímpar'.format(numero_int))

parImpar(numero_int)