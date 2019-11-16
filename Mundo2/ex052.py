"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

def numeroPrimo():
    contador = 0
    numero = int(input('Número: '))
    for x in range(1, numero + 1):
        if numero % x == 0:
            contador += 1
    
    if contador >= 1:
        print('Número primo')
    elif contador > 2:
        print('Não é primo')
    elif contador < 1:
        print('Número inválido')        
    
    print('O número {} foi dividido {} vezes'.format(numero, contador))
numeroPrimo()