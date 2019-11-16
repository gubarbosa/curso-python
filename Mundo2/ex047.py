""" Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""
from termcolor import colored
from time import sleep

programa = "  CONTADOR DE PARES  "
def pares():
    print(colored('=') * len(programa))
    print(colored(programa, "blue"))
    print(colored('=') * len(programa))
    sleep(1)
    print(colored('Calculando pares..', "red"))
    for i in range(2, 51, 2):
        print(i, end=' ')
    
pares()