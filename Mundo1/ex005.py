"""Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor."""
numero_int = int(input('Digite um número inteiro: '))

def sucessor_Antecessor(numero_int):
    antecessor = numero_int - 1
    sucessor = numero_int + 1
    print(f'Sucessor de {numero_int} é {sucessor}')
    print(f'Antecessor de {numero_int} é {antecessor}')
    return antecessor, sucessor

sucessor_Antecessor(numero_int)