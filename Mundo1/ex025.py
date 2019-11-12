"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""
nome_pessoa = str(input('Nome da pessoa: ')).strip().upper()

def verificaSilva(nome_pessoa):
    if 'SILVA' in nome_pessoa:
        print('A pessoa tem Silva no nome')
    else:
        print('A pessoa não tem Silva no nome')

verificaSilva(nome_pessoa)