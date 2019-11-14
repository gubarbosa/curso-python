"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

from termcolor import colored
from time import sleep
programa = "  LOJA DO KAKO  "

def valorProduto():
    print(colored("=", "blue") * len(programa))
    print(colored(programa, "yellow"))
    print(colored("=", "blue") * len(programa))
    preco_formal = float(input('Preço do produto: R$'))

    print(colored("  FORMA DE PAGAMENTO:  \n"
                "1 - à vista dinheiro/cheque: 10% de desconto \n"
                "2 - à vista no cartão: 5% de desconto \n"
                "3 - em até 2x no cartão: preço formal \n"
                "4 - 3x ou mais no cartão: 20% de juros", "magenta"))

    sleep(3)
    forma_pagamento = int(input('Seleciona a forma de pagamento: '))
    if forma_pagamento == 1:
        preco = preco_formal - (10/100 * preco_formal)
        desconto = (10/100 * preco_formal)
        print(colored("O valor total das compras é de R$ {:.2f}, utilizando a 1ª forma de pagamento, há um desconto de R${:.2f} e o valor desce para R${:.2f}".format(preco_formal, desconto, preco), "yellow"))
    elif forma_pagamento == 2:
        preco = preco_formal - (5/100 * preco_formal)
        desconto = (5/100 * preco_formal)
        print(colored("O valor total das compras é de R$ {:.2f}, utilizando a 2ª forma de pagamento, há um desconto de R${:.2f} o valor desce para R$ {:.2f}".format(preco_formal, desconto, preco), "yellow"))
    elif forma_pagamento == 3:
        parcelas = preco_formal / 2
        print(colored("O valor total das compras é de R$ {:.2f}, utilizando a 3ª forma de pagamento, o valor ficará em 2x de R${:.2f}".format(preco_formal, parcelas), "blue"))
    elif forma_pagamento == 4:
        parcelas = int(input('Em quantas parcelas? '))
        preco = preco_formal + (20/100 * preco_formal)
        aumento = (20/100 * preco_formal)
        print(colored("O valor total das compras é de R$ {:.2f}, utilizando a 4ª forma de pagamento, o valor ficará em {}x de RS{:.2F}.\nHá um aumento de R${:.2f} e o valor sobe para R$ {:.2f}".format(preco_formal, parcelas, preco / parcelas, aumento, preco), "red"))
    else:
        print(colored('Forma de pagamento inválida!', "red"))

valorProduto()

    