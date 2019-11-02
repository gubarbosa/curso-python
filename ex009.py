"""Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada."""

numero1 = int(input('Digite um número para ver sua tabuada: '))

def tabuada(numero1):
    contador = 0
    print('-' * 12)
    while contador < 11:
        print('{} x {:2} = {}'.format(numero1, contador, numero1 * contador))
        contador += 1
    print('-' * 12)

tabuada(numero1)

