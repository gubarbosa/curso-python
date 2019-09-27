from random import *

numero = randint(0, 5)
chute = int(input('Escolha um número entre 0 e 5:'))
if numero == chute:
    print('Você acertou'
else:
    print('Você errou')


velocidade_carro = float(input('Digite a velocidade do seu carro:'))
limite = float(80)
multa = float((velocidade_carro - limite) * 7)
if velocidade_carro > 80:
    print('Você foi multado, valor: R${:.2f}'.format(multa))
else:
    print("Você não foi multado")



num = int(input('Digite um número inteiro:'))
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')


distancia = float(input('Digite a distância de sua viagem:'))
if distancia <= 200:
    print('O valor da passagem será de: R${}'.format(0.5 * distancia))
else:
    print('O valor da passagem será de: R${}'.format(0.45 * distancia))


ano = int(input('Digite um ano:'))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano é bissexto')
elif ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')


a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
c = int(input('Digite outro número:'))
if a > b and a > c or b > a and b > c or c > a and c > b:
    print('O número {} é o maior entre eles'.format(a))
elif a < b and a < c or b < a and b < c or c < a and c < b:
    print('O número {} é o menor entre eles'.format(a))
else:
    print('Os números são iguais')


salario = float(input('Digite o valor do seu salário:'))
if salario > 1.250:
    print('Você irá receber um aumento de: R${:.3f}'.format(salario*0.1))
else:
    print('Você irá receber um aumento de: R${:.3f}'.format(salario*0.15))

reta1 = int(input('Comprimento da reta 1:'))
reta2 = int(input('Comprimento da reta 2:'))
reta3 = int(input('Comprimento da reta 3:'))
if reta1 + reta2 > reta3 or reta1 + reta3 > reta2 or reta2 + reta3 > reta1 or reta1 == reta2 == reta3:
    print('É um triângulo')
else:
    print('Não é triângulo')