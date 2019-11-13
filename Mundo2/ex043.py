"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

from termcolor import colored
from time import sleep
programa = "  ÍNDICE DE MASSA CORPORAL  "

def IMC():
    print(colored('=', 'blue') * len(programa))
    print(colored(programa, 'green'))
    print(colored('- IMC abaixo de 18,5: Abaixo do Peso \n'
                '- Entre 18,5 e 25: Peso Ideal \n'
                '- 25 até 30: Sobrepeso \n'
                '- 30 até 40: Obesidade \n'
                '- Acima de 40: Obesidade Mórbida','magenta'))
    print(colored('=', 'blue') * len(programa))

    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura ** 2)
    print(colored('Calculando IMC e seu status..', 'blue'))
    sleep(2)

    if imc < 18.5:
        categoria = 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        categoria = 'Peso ideal'
    elif imc >= 25 and imc < 30:
        categoria = 'Sobrepeso'
    elif imc >= 30 and imc < 40:
        categoria = 'Obesidade'
    else:
        categoria = 'Obesidade mórbida'
    print(colored('Com {:.1f}kg e {:.2f}m, seu IMC tem valor de {:.1f} e categoria: {}'.format(peso, altura, imc, categoria), "yellow"))

IMC()
