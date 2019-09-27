nome = str.capitalize(input('Qual é o seu nome:'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão bosta!')
print('Tenha um bom dia {}'.format(nome))


n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media >= 7:
    print('Parabéns, você foi aprovado')
else:
    print('Você não atingiu a média, estude mais!')

