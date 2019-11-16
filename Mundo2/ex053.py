""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""
programa = "  DETECTA PALÍNDROMO  "
from termcolor import colored
from time import sleep

def detectaPalindromo():
    frase = str(input('Digite uma frase:')).strip().replace(' ', "")
    if frase == frase[::-1]:
        print('É palíndromo')
    else:
        print('Não é palíndromo')

    

detectaPalindromo()