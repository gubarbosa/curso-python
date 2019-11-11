"""Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente."""

nome_completo = str(input('Digite seu nome completo: ')).strip().split()

def nomeCompleto(nome_completo):
    primeiro_nome = nome_completo[0].capitalize()
    ultimo_nome = nome_completo[-1].capitalize()
    print('Seu primeiro nome é {} \n'
          'Último nome é {}'.format(primeiro_nome, ultimo_nome))

nomeCompleto(nome_completo)
