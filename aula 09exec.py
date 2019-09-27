nome = input('Qual é o seu nome completo:')
print(nome.upper())
print(nome.lower())
nome_dividido = nome.split()
print(len(''.join(nome_dividido)))
print(len(nome_dividido[0]))


cidade = input('Digite o nome de uma cidade:').strip()
print(cidade[0:5].upper() == 'SANTO')

nome = input('Digite o seu nome:').strip()
print(nome[0:5].upper() == 'SILVA')

frase = input('Digite uma frase:')
print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))

nome_completo = input('Digite seu nome completo:').strip().split()
print('O seu primeiro nome é: {}'.format(nome_completo[0]))
print('O seu segundo nome é: {}'.format(nome_completo[1]))