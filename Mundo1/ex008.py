"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""
metros = float(input('Digite um valor em metros: '))
centimetros = (metros * 100)
milimetros = (metros * 1000)
km = (metros / 1000)
hm = (metros / 100)
dam = (metros / 10)
dm = (metros * 10)

def conversaoMedidas(metros):
    print('O valor de {:.1f} metros é igual a: \n {:.1f} centímetros \n {:.1f} milímetros'.format(metros, centimetros, milimetros))
    print(' {:.1f}km \n {:.1f}hm \n {:.1f}dam \n {:.1f}dm'.format(km, hm, dam, dm))
    return centimetros, milimetros, km, hm, dam, dm

conversaoMedidas(metros)