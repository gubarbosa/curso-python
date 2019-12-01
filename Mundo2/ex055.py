"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

def pesos():
    lista = []
    for x in range(1, 6):
        x += 1
        ano = int(input('Digite seu peso: '))
        lista.append(ano)

    print('Maior peso lido: {}'.format(max(lista)))
    print('Menor peso lido: {}'.format(min(lista)))
pesos()


