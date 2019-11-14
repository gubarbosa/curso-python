"""Crie um programa que faça o computador jogar Jokenpô com você."""

from termcolor import colored
from time import sleep
import random
programa = "  JOKENPÔ  "

def jokenpô():
    print(colored("=", "red") * len(programa))
    print(colored(programa, "magenta"))
    print(colored("=", "red") * len(programa))

    usuario = str(input('Seu nome: '))
    lista = ['Pedra', 'Papel', 'Tesoura']
    resposta_pc = random.choice(lista)
    resposta_user = int(input('[1] - Pedra\n'
                              '[2] - Papel\n'
                              '[3] - Tesoura\n'
                              'Sua escolha: '))

    print(colored("JO", "blue"))
    sleep(1)
    print(colored("KEN", "blue"))             
    sleep(1)
    print(colored('PÔ', "blue")) 
   
    if resposta_pc == lista[0] and resposta_user == 1:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. EMPATE".format(resposta_pc, 'Pedra'), "white"))
    elif resposta_pc == lista[0] and resposta_user == 2:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. Vitória de {}".format(resposta_pc, 'Papel', usuario), "yellow"))
    elif resposta_pc == lista[0] and resposta_user == 3:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. Vitória do PC!".format(resposta_pc, "Tesoura"), "red"))
    elif resposta_pc == lista[1] and resposta_user == 1:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. Vitória do PC!".format(resposta_pc, "Pedra"), "red"))
    elif resposta_pc == lista[1] and resposta_user == 2:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. EMPATE".format(resposta_pc, "Papel"), "white"))
    elif resposta_pc == lista[1] and resposta_user == 3:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. Vitória de {}".format(resposta_pc, "Tesoura", usuario), "yellow"))
    elif resposta_pc == lista[2] and resposta_user == 1:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. Vitória de {}".format(resposta_pc, "Pedra", usuario), 'yellow'))
    elif resposta_pc == lista[2] and resposta_user == 2:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. Vitória do PC!".format(resposta_pc, "Papel"), "red"))
    elif resposta_pc == lista[2] and resposta_user == 3:
        resultado = print(colored("Como a máquina escolheu {} e você escolheu {}.. EMPATE".format(resposta_pc, "Tesoura"), "white"))      

    return resultado

jokenpô()
    