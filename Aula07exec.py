n = int(input('Digite um número inteiro:'))
num = int(input('Digite outro número inteiro:'))
print('O Dobro de {} é: {}. \n O Triplo de {} é: {}. \n A Raiz Quadrada de {} é: {}'.format(num, num*2, num, num*3, num, num**0.5))

n1 = int(input('Digite sua primeira nota:'))
n2 = int(input('Digite a segunda nota:'))
print('A sua média bimestral é {}!'.format((n1 + n2) / 2))

d1 = int(input('Digite um valor que será válido em metros:'))
print('O valor {} em centímetros vale {}, já em milímetros vale {}!'.format(d1,d1 * 100, d1*1000))

n1 = int(input('Digite um número para visualizar a sua tabuada completa:'))
print('{} x 0 = {}, {} x 1 = {}, {} x 2 = {}, {} x 3 = {}, {} x 4 = {}, {} x 5 = {}, {} x 6 = {}, {} x 7 = {}, {} x 8 = {}, {} x 9 = {}, {} x 10 = {}'.format(n1,n1*0,n1,n1*1,n1,n1*2,n1,n1*3,n1,n1*4,n1,n1*5,n1,n1*6,n1,n1*7,n1,n1*8,n1,n1*9,n1,n1*10))

n1 = int(input('Digite quantos reais você tem na carteira:'))
print('Com esse capital, no momento você pode comprar {} dólares'.format(n1/3.72))

n1 = int(input('Digite a altura de sua parede em metros:'))
n2 = int(input('Digita a largura de sua parede em metros:'))
a = n1*n2
print('A área de sua parede vale: {} metros quadrados!'.format(a))
print('Para pintar sua parede você precisa de {} litros de tinta'.format(0.5*a))

n1 = int(input('Digite o valor do computador:'))
print('Na promoção, com 5% de desconto, o computador sai por: {}'.format(n1 - (n1*5)/100))

n1 = int(input('O seu salário é:'))
print('Com o aumento de 15%, seu salário é: {}'.format(n1 + n1*15/100))