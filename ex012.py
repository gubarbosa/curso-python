""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""
salario_funcionario = float(input('Salário do funcionário: '))

def aumentoSalario(salario_funcionario):
    aumento = salario_funcionario * 15/100
    novo_salario = salario_funcionario + aumento
    print('O salário de R${:.2f} com um aumento de 15% irá para R${:.2f}'.format(salario_funcionario, novo_salario))
    return novo_salario

aumentoSalario(salario_funcionario)