""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

from termcolor import colored

def aumentoSalario():
    salario = int(input('Salário do funcionário: '))
    if salario > 1250:
        aumento = salario * (10/100)
    else:
        aumento = salario * (15/100)
    print(colored('Como seu salário é de R${:.2f}, você irá ganhar agora: R${:.2f}'.format(salario, aumento + salario),'green'))
aumentoSalario()