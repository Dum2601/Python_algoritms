# Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

a = int(input('Informe o primeiro valor inteiro: \n'))
b = int(input('Informe o segundo valor inteiro \n'))
c = int(input('Informe o terceiro valor inteiro \n'))

numbers = [a, b, c]
numbers.sort(reverse = True)

print(numbers)