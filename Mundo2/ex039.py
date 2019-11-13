""""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
from termcolor import colored
programa = '  ALISTAMENTO MILITAR  '

def alistamentoMilitar():
    print(colored('-', 'magenta') * len(programa))
    print(colored(programa, 'green'))
    print(colored('-', 'magenta') * len(programa))

    ano_nascimento = int(input('Digite o ano que você nasceu: '))
    idade = date.today().year - ano_nascimento

    if idade < 18:
        saldo = 18 - idade
        anos = "anos" if saldo > 1 else "ano"
        print(colored('Você só pode se alistar com 18 anos! Como você tem {} anos, ainda faltam {} {}'.format(idade, 18 - idade, anos), 'blue'))
        print(colored('Seu alistamento será em {}'.format(ano_nascimento + 18), 'blue'))
    elif idade == 18:
        print(colored('Você está pronto para se alistar, pois tem {} anos'.format(idade), 'yellow'))
    elif idade > 18:
        saldo = idade - 18
        anos = "anos" if saldo > 1 else "ano"
        print(colored('Já se passaram {} {} do momento certo para se alistar amigo!'.format(idade - 18, anos), 'red'))
        print(colored('Seu alistamento deveria ter sido em {}'.format(ano_nascimento + 18), 'red'))

alistamentoMilitar()
