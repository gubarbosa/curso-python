"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

km_percorridos = float(input('Quilômetros percorridos: '))
dias_alugado = int(input('Dias alugado: '))

def aluguelCarro(km_percorridos, dias_alugado):
    preco_dias = 60 * dias_alugado
    preco_km = km_percorridos * 0.15
    preco_total = preco_dias + preco_km
    print('Sabendo que foram andados {:.1f}km por {:.0f} dias com o carro, o valor do aluguel é de R${:.2f}'.format(km_percorridos, dias_alugado, preco_total))
    return preco_total

aluguelCarro(km_percorridos, dias_alugado)