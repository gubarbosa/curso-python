""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""
from time import sleep
from termcolor import colored
from datetime import date
programa = "  CATEGORIA DE NATAÇÃO  "

def categoriaNatacao():
    print(colored('=', 'white') * len(programa))
    print(colored(programa, 'blue'))
    print(colored('=', 'white') * len(programa))

    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - ano_nascimento

    print(colored("Calculando categoria..", "magenta"))
    sleep(2)

    if idade <= 9:
        categoria = 'MIRIM'
    elif idade <= 14:
        categoria = "INFANTIL"
    elif idade <= 19:
        categoria = "JÚNIOR"
    elif idade <= 25:
        categoria = "SÊNIOR"
    else:
        categoria = "MASTER"
    print(colored('Por ter {} anos, a sua categoria é: {}'.format(idade, categoria), "yellow"))

categoriaNatacao()