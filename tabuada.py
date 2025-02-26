# 19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10.

tab = 1

for x in range(1, 11):
    for x in range(1, 11):
        print(f'{x} * {tab} = {x*tab}')
    tab += 1
    print(10 * '-')
    print(' ')
