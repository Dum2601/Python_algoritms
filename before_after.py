# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

def read_number(a):
    try:
        a = int(a)
        before = a - 1
        after = a + 1
        
    except Exception as e:
        print(f'Ocorreu o erro: {e}')
    
    return before, after
    
num = input('informe um número para ser analisado: \n')

before, after = read_number(num)

print(f'O número informado é: {num} \n',
f'O sucessor é: {after} \n',
f'O antecessor é: {before} \n')
