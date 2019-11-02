""" Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""
algo = input('Digite algum dado: ')
def informacoesAlgo(algo):
    tipo_primitivo = type(algo)
    espacos = algo.isspace()
    numero = algo.isnumeric()
    letra = algo.isalpha()
    numero_e_letra = algo.isalnum()
    maiuscula = algo.isupper()
    minuscula = algo.islower()
    capitalizado = algo.istitle()
    print(f'O tipo primitivo de {algo} é {tipo_primitivo}')
    print(f'{algo} só contêm espaços? {espacos}')
    print(f'{algo} é só numérico? {numero}')
    print(f'{algo} é só alfabético? {letra}')
    print(f'{algo} é alphanumérico? {numero_e_letra}')
    print(f'{algo} está em maiúsculas? {maiuscula}')
    print(f'{algo} está em minúsculas? {minuscula}')
    print(f'{algo} está capitalizado? {capitalizado}')
    return algo

informacoesAlgo(algo)