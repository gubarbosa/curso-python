import math
import random
import pygame

n1 = (float(input('Digite um número real qualquer:')))
print('O número {} possui como porção inteira {}'.format(n1, int(n1)))

n1 = (int(input('Digite o valor do cateto oposto de um triângulo retângulo:')))
n2 = (int(input('A seguir, escreva o valor do cateto adjacente desse triângulo:')))
h = math.sqrt(n2 ** 2 + n1 ** 2)
h1 = math.hypot(n1, n2)
print('De acordo com os catetos, o valor da hipotenusa vale: {:.2f}'.format(h))
print('A hipotenusa vale {:.2f}'.format(h1))

a1 = int(input('Digite o valor de um ângulo qualquer:'))
sen = math.sin(a1)
cos = math.cos(a1)
tan = math.tan(a1)
print('O valor do seno desse número é: {:.2f}'.format(sen))
print('O valor do cosseno desse número é: {:.2f}'.format(cos))
print('O valor da tangente desse número é:{:.2f}'.format(tan))

n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
nr = [n1,n2,n3,n4]
n = random.choice(nr)
s = random.shuffle(nr)
print('O aluno escolhido para apagar o quadro é {}!'.format(n))

n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno'))
n4 = str(input('Quarto aluno:'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A sequência para apagar o quadro é: {}'.format(lista))

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
