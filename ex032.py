"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from termcolor import colored
from time import sleep
from datetime import date

def anoBissexto():
    programa = '  VERIFICADOR ANO BISSEXTO  '
    print(colored('-','white') * len(programa))
    print(colored(programa, 'green'))
    print(colored('-','white') * len(programa))
    ano = int(input(colored('Digite um ano para verificar, ou 0 para verificar o ano atual: ','magenta')))
    if ano == 0:
        ano = date.today().year
    print(colored('Verificando ano..','blue'))
    sleep(2)
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print(colored('É ano bissexto!','yellow'))
    else:
        print(colored('Não é ano bissexto!','red'))

anoBissexto()