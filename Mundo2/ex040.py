"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

from time import sleep
from termcolor import colored
programa = '  BOLETIM  '

def media():
    print(colored('=', 'grey') * len(programa))
    print(colored(programa, 'yellow'))
    print(colored('=', 'grey') * len(programa))

    aluno = str(input('Nome do aluno(a): '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    print(colored('Calculando média..', 'magenta'))
    sleep(2)
    media = (nota1 + nota2) / 2
    print(colored('Média final: {:.1f}'.format(media), 'yellow'))
    sleep(2)
    print(colored('Calculando resultado final!', 'white'))
    sleep(3)

    if media >= 7:
        print(colored('Parabéns {}! você foi APROVADO(A)!'.format(aluno), 'green'))
    elif media >= 5 and media <= 6.9:
        print(colored('Atenção {}!, você está em recuperação!!'.format(aluno), 'blue'))
    elif media < 5:
        print(colored('{}, infelizmente você foi reprovado(a)'.format(aluno), 'red'))

media()