"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""
dinheiro = float(input('Dinheiro que a pessoa tem: '))

def dólares(dinheiro):
    dolares = dinheiro / 3.99
    print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, dolares))
    return dolares

dólares(dinheiro)