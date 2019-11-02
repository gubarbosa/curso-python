"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""
from math import sqrt, hypot, pow
cateto_oposto = int(input('Cateto oposto: '))
cateto_adjacente = int(input('Adjacente: '))

def hipotenusa(cateto_oposto, cateto_adjacente):
    hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))    #math.hypot(cateto_oposto, cateto_adjacente)
    print('Tendo como {} de cateto oposto e {} de cateto adjancete, a hipotenusa é igual a {:.0f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))
    return hipotenusa

hipotenusa(cateto_oposto, cateto_adjacente)
