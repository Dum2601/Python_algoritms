# Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

num = int(input('Informe um número inteiro: \n'))

while type(num) != int:
    print('Apenas números do tipo inteiro serão aceitos!')
    num = int(input('Informe um número inteiro: \n'))

before = num - 1
after = num + 1

print(f'O valor informado foi {num}, logo seu antecessor é o {before} e seu sucessor é {after}')
