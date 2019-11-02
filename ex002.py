"""Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas."""

nome_pessoa = str(input('Digite seu nome: '))

def boasVindas(nome_pessoa):
    msg_boas_vindas = 'Seja bem-vindo {}!!'.format(nome_pessoa)
    print(msg_boas_vindas)
    return msg_boas_vindas

boasVindas(nome_pessoa)