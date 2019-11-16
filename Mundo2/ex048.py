"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500."""
programa = "SOMA DE MÚLTIPLOS DE 3"
from termcolor import colored
from time import sleep

def somaMultiplos():
    print(colored("=", "blue") * len(programa))
    print(colored(programa, "red"))
    print(colored("=", "blue") * len(programa))
    sleep(1)
    soma = 0
    cont = 0
    for i in range(1, 501):
        if i % 2 != 0 and i % 3 == 0:
            soma += i
            cont += 1
    
    print(colored(f'A soma dos {cont} valores encontrados é {soma}', "yellow"))

somaMultiplos()