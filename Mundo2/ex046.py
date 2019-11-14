"""Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""
from time import sleep
from termcolor import colored

def contagemRegressiva():
    for numeros in range(10, -1, -1):
        print(numeros)
        sleep(1)

    # for numeros in range(0, segundos):
    #     print(segundos)
    #     sleep(1)
    #     segundos -= 1
    print(colored('FOGOS DE ARTIFÍCIO!!', "magenta"))

contagemRegressiva()