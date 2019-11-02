""" Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
 e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
largura_parede = float(input('Largura parede: '))
altura_parede = float(input('Altura parede: '))

def tintaPintura(largura_parede, altura_parede):
    area_parede = largura_parede * altura_parede
    tinta = area_parede / 2
    print('Para pintar {:.0f} m² é necessário {:.0f} litros de tinta'.format(area_parede, tinta))
    return tinta

tintaPintura(largura_parede, altura_parede)
