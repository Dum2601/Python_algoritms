# 17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

# Fórmula: C = (5 * ( F-32) / 9)

f = float(input('Informe a temperatura em farenheit> \n'))
c = (5 * ( f-32) / 9)

print(f'O valor equivale a {c} C')
