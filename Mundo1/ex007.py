"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

def mediaAluno(nota1, nota2):
    print('Média do aluno: {:.1f}'.format(media))
    return media

mediaAluno(nota1, nota2)