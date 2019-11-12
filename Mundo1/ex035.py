""": Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

from termcolor import colored
from time import sleep

programa = '  VERIFICAÇÃO DE TRIÂNGULO  '

def verificaTriangulo():
    print(colored('*', 'red') * len(programa))
    print(colored(programa, 'yellow'))
    print(colored('*', 'red') * len(programa))
    reta1 = int(input('Reta 1: '))
    reta2 = int(input('Reta 2: '))
    reta3 = int(input('Reta 3: '))
    print(colored('Analisando as possibilidades de triângulo..', 'magenta'))
    sleep(3)
    if reta1 >= reta2 + reta3 or reta2 >= reta1 + reta3 or reta3 >= reta1 + reta2:
        print(colored('Não é triângulo! Tente novamente..', 'red'))
    else:
        print(colored('As dimensões de {}, {} e {} podem formar um triângulo! Parabéns!'.format(reta1, reta2, reta3), 'yellow'))

verificaTriangulo()