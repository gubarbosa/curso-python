"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

programa = "ANALISADOR COMPLETO"
from termcolor import colored
from time import sleep

def analisador():
    media = []
    for x in range(1, 5):
        x += 1
        #nome = str(input('Qual é o seu nome? '))
        idade = int(input('Quantos anos você tem? '))
        #sexo = str(input('Seu sexo: [M] - Mulher \n'
        #                                    '[H] - Homem')).upper().strip()
        media.append(idade)

    media_idade = sum(media) / len(media)
    print(media_idade)  

analisador()