"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome_pessoa = str(input('Digite seu nome: '))
nome_espacos = nome_pessoa.strip()
nome_split = nome_espacos.split(' ')

def nome(nome_pessoa):
    nome_upper = nome_pessoa.upper()
    nome_lower = nome_pessoa.lower()

    print('Seu nome maiúsculo é {}'.format(nome_upper))
    print('Seu nome minúsculo é {}'.format(nome_lower))
    print('Seu nome completo possui {} letras'.format(len(nome_espacos) - nome_espacos.count(' ')))
    print('Seu nome possui {} letras'.format(len(nome_split[0])))      #nome_espacos.find(' ')

nome(nome_pessoa)