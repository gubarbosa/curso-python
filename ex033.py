"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

def comparaNumeros():
    numero1 = int(input('Primeiro número: '))
    numero2 = int(input('Segundo número: '))
    numero3 = int(input('Terceiro número: '))
    if numero1 < numero2 and numero1 < numero3:
        print('O número {} é o menor número'.format(numero1))
    elif numero2 < numero1 and numero2 < numero3:
        print('O número {} é o menor número'.format(numero2))
    elif numero3 < numero1 and numero3 < numero2:
        print('O número {} é o menor número'.format(numero3))

    if numero1 > numero2 and numero1 > numero3:
        print('O número {} é o maior número'.format(numero1))
    elif numero2 > numero3 and numero2 > numero1:
        print('O número {} é o maior número'.format(numero2))
    elif numero3 > numero2 and numero3 > numero1:
        print('O número {] é o maior número'.format(numero3))

comparaNumeros()