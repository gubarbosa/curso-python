""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""
from time import sleep
from termcolor import colored
programa = '  APROVA EMPRÉSTIMO  '

def aprovaEmprestimo():
    print(colored('*', 'magenta') * len(programa))
    print(colored(programa, 'green'))
    print(colored('*', 'magenta') * len(programa))

    casa = float(input('Valor da casa: R$'))
    salario = float(input('Salário do comprador: R$'))
    anos_para_pagar = int(input('Em quantos anos irá pagar? R$'))
    prestacao_mensal = casa / (anos_para_pagar * 12)

    print(colored('Analisando empréstimo..', 'blue'))
    sleep(3)

    print(colored('Para pagar a casa no valor de R${:.2f} em {} anos, a prestação mensal é de R${:.2f}'.format(casa, anos_para_pagar, prestacao_mensal), 'red'))
    if prestacao_mensal <= (30/100) * salario:
        print(colored('Empréstimo bancário aceito!', 'yellow'))
    else:
        print(colored('Empréstimo negado!', 'red'))

aprovaEmprestimo()



