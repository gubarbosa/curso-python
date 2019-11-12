"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

cidade = str(input('Nome da cidade: ')).upper().strip().split()

def verificaSanto(cidade):
    if 'SANTO' == cidade[0]:
        print('A cidade começa com Santo no nome')
        return True
    else:
        print('A cidade não começa com Santo no nome')
        return False

verificaSanto(cidade)
