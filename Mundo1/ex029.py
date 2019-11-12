"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

from termcolor import colored
from time import sleep

def blitz():
    print(colored('-=-','white')*10)
    print(colored('BEM-VINDO A BLITZ DO PARAÍSO','red'))
    print(colored('-=-','white')*10)
    velocidade = int(input('Em que velocidade você estava nessa avenida? '))
    multa = (velocidade - 80) * 7
    if velocidade > 80:
        sleep(3)
        print(colored('Calculando multa.. =(','magenta'))
        sleep(3)
        print(colored('Como você ultrapassou os 80km/h será multado com R${:.2f}'.format(multa),'red'))
        print(colored('Tenha maior atenção no trânsito!','green'))
    else:
        print(colored('A princípio, está tudo correto..um momento','yellow'))
        sleep(3)
        print(colored('Parabéns! Você está dirigindo com consciência.','yellow'))

blitz()