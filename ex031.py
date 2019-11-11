"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

from time import sleep
from termcolor import colored
cobrador = '  COBRADOR DE PASSAGEM  '

def custoViagem():
    print(colored('*','green')* len(cobrador))
    print(colored(cobrador,'magenta'))
    print(colored('*','green')* len(cobrador))
    distancia = float(input('Distância da viagem: '))
    print(colored('Calculando preço..', 'yellow'))
    sleep(3)
    preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
    print(colored('Viajando {}km, o preço da passagem é de R${:.2f}'.format(distancia, preco),'red'))
    return preco

custoViagem()