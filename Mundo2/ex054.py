"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

def maioridade():
    atual = date.today().year
    contador_maior = 0
    contador_menor = 0
    for x in range(0, 7):
        x += 1
        ano = int(input('Ano de nascimento da {}ª pessoa: '.format(x)))
        idade = atual - ano
        if idade >= 18:
            contador_maior += 1
        else:
            contador_menor += 1
    
    print('{} são de maior e {} sao de menor'.format(contador_maior, contador_menor))

maioridade()