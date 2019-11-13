"""Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
from termcolor import colored
from time import sleep
programa = '  Conversor de bases numéricas!  '

def basesNumericas():
    print(colored('=', 'red') * len(programa))
    print(colored(programa, 'blue'))
    sleep(1)
    print(colored('O objetivo é converter um número \ninteiro em alguma base numérica: \nbinário, octal ou hexadecimal', 'yellow'))
    print(colored('=', 'red') * len(programa))
    sleep(2)

    numero = int(input('Digite um número inteiro: '))
    base_conversao = int(input('Escolha a base de conversão: 1 p/ binário, 2 p/ octal e 3 p/ hexadecimal: '))

    if base_conversao == 1:
        base = 'binário'
        numero_convertido = bin(numero)
    elif base_conversao == 2:
        base = 'octal'
        numero_convertido = oct(numero)
    elif base_conversao == 3:
        base = 'hexadecimal'
        numero_convertido = hex(numero)
    else:
        print(colored('Opção inválida! Tente novamente', 'red'))

    print(colored('Convertendo {} em {}..'.format(numero, base), 'blue'))
    sleep(2)
    print(colored('O número {} em {} é {}'.format(numero, base, numero_convertido[2:]), 'yellow'))

basesNumericas()