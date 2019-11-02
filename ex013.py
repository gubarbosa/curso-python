""" Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."""
celsius = float(input('Temperatura em Cº: '))

def celsius_Fahrenheit(celsius):
    temp_fah = 9 / 5 * celsius + 32
    print('A temperatura de {}ºC equivale a {}ºF'.format(celsius, temp_fah))
    return temp_fah

celsius_Fahrenheit(celsius)