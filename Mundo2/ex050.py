"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""
from termcolor import colored
from time import sleep
programa = "  SOMA DOS PARES  "

def somaPares():
    print(colored("*", "blue") * len(programa))
    print(colored(programa, "white"))
    print(colored("*", "blue") * len(programa))
    soma = 0

    for x in range(1, 7):
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            soma += numero
    print(colored('Fazendo a soma dos pares..', "yellow"))
    sleep(1)
    print(colored("Dos números apresentados, {} são pares, a soma dos pares é {}".format(numero, soma), "yellow"))

somaPares()