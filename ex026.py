"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""
frase = str(input('Digite a frase: ')).strip().upper()

def ocorrenciaA(frase):
    qntd_a = frase.count('A')
    posicao_1 = frase.find('A')
    posicao_2 = frase.rfind('A')
    print('A letra a aparece {} vezes \n'
          'A primeira vez na posição {} \n'
          'Última vez na posição {}'.format(qntd_a, posicao_1 + 1, posicao_2 + 1))

ocorrenciaA(frase)
