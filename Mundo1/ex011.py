"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""
preco_produto = float(input('Preço produto: '))

def descontoProduto(preco_produto):
    preco_com_desconto = preco_produto - (preco_produto * 5/100)
    print('O produto que custava R${:.0f}.00, com 5% de desconto, está custando R${:.0f}.00'.format(preco_produto, preco_com_desconto))
    return preco_com_desconto

descontoProduto(preco_produto)