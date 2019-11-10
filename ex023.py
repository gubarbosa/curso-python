""" Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""
#numero = str(input('Número de 0 a 9999: '))

#def digitosSeparados(numero):
  #  milhar = numero[0]
  #  centena = numero[1]
 #   dezena = numero[2]
  #  unidade = numero[3]
  #  print('Milhar: {}  \n'
  #        'Centena: {}\n'
  #        'Dezena: {} \n'
 #         'Unidade: {}'.format(milhar, centena, dezena, unidade))
#
#digitosSeparados(numero)

numero_int = int(input('Número de 0 a 9999: '))
def digitoSeparado(numero_int):
    milhar_int = numero_int // 1000 % 10
    centena_int = numero_int // 100 % 10
    dezena_int = numero_int // 10 % 10
    unidade_int = numero_int // 1 % 10
    print('Milhar: {}  \n'
          'Centena: {} \n'
          'Dezena: {} \n'
          'Unidade: {}'.format(milhar_int, centena_int, dezena_int, unidade_int))

digitoSeparado(numero_int)