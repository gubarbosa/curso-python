"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""
numero = int(input('Digite um número: '))
def operacoes(numero):
    dobro = numero * 2
    triplo = numero * 3
    raiz_quadrada = pow(numero, 0.5)    #numero ** 0.5
    print(' Seu dobro: {} \n Seu triplo: {} \n Raiz quadrada: {:.2f}'.format(dobro, triplo, raiz_quadrada))

operacoes(numero)