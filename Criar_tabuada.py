# 20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

value = int(input('Informe o valor desejado: \n'))

for x in range(1, 11):
    print(f'{value} x {x} = {value * x}')
