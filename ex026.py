"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""
frase = str(input('Digite a frase: '))

def ocorrenciaA(frase):
    qntd_a = frase.count('a')
    posicao_1 = frase.find('a')
    