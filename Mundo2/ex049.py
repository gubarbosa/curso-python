"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""
programa = "  TABUDA  "
from termcolor import colored
from time import sleep

def tabuada():
    print(colored('*', "blue") * len(programa))
    print(colored(programa, "white"))
    print(colored('*', "blue") * len(programa))
    sleep(1)
    numero = int(input(colored('Escolha o número da tabuada: ', "yellow")))
    print(colored('Calculando tabuada..', "magenta"))
    sleep(1)
    for x in range(0, 11):
        print(colored('{} x {:2} = {}'.format(numero, x, numero * x), "blue"))

tabuada()