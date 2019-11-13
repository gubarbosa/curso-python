"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

from termcolor import colored
programa = '  COMPARADOR DE NÚMEROS  '

def comparaNumeros():
    print(colored('-', 'blue') * len(programa))
    print(colored(programa, 'red'))
    print(colored('-', 'blue') * len(programa))

    numero1 = int(input('Primeiro número: '))
    numero2 = int(input('Segundo número: '))
    if numero1 > numero2:
        print(colored('O primeiro valor é maior', 'yellow'))
    elif numero2 > numero1:
        print(colored('O segundo valor é maior', 'yellow'))
    else:
        print(colored('Não existe valor maior, são iguais', 'red'))

comparaNumeros()
