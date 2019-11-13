"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""


def classificacaoTriangulo():
    reta1 = int(input('Reta 1: '))
    reta2 = int(input('Reta 2: '))
    reta3 = int(input('Reta 3: '))

    if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
        if reta1 == reta2 == reta3:
            classificacao = 'EQUILÁTERO'
        elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
            classificacao = 'ISÓSCELES'
        elif reta1 != reta2 != reta3 != reta1:
            classificacao = 'ESCALENO'
        print('É um triângulo {}'.format(classificacao))
    else:
        print('Não é triângulo')

classificacaoTriangulo()