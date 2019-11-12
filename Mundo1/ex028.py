""" Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import choice
from time import sleep
from termcolor import colored

lista = [0, 1, 2, 3, 4, 5]

def numeroAleatorio():
    print(colored('- ','magenta')* 25)
    print(colored(' Irei pensar em um número de 0 a 5.. tente adivinhar!!','blue'))
    print(colored('- ','magenta')* 25)
    print(colored('PROCESSANDO..','yellow'))
    sleep(3)
    numero_aleatorio = choice(lista)
    resposta = int(input('Digite um número entre 0 e 5: '))
    print(colored('Um momento..', 'yellow'))
    sleep(5)
    if numero_aleatorio == resposta:
        print(colored('Parabéns! Você ganhou o jogo','green'))
    else:
        print(colored('Você perdeu, tente novamente!','red'))

numeroAleatorio()