"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
import math
angulo = int(input("Digite um ângulo: "))

def trigonometria(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    print('Dado ângulo {}º, segue os valores: \n'
          'Seno: {:.2f}\n'
          'Cosseno: {:.2f}\n'
          'Tangente: {:.2f}'.format(angulo, seno, cosseno, tangente))
    return seno, cosseno, tangente

trigonometria(angulo)