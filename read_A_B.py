# Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
# Language used: PT-BR

a = int(input('Digite o valor de A: \n'))
b = int(input('Digite o valor de B: \n'))
c = int(input('Digite o valor de C: \n'))


sum = a + b

if type(sum) == int:
    print(f'A soma dos valores informados é: {sum}')
else: 
    print('Insira um valor válido!')

if sum < c:
    print(f'A soma é menor que {c}')
elif sum > c:
    print(f'A soma é maior que {c}')
else:
    print('O valor informado não é valido!')