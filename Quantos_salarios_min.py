# 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 

# usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

def calc_sar(*sar): # Argumentos para não gerar nenhum erro caso coloque mais parâmetros que o permitido
    if len(sar) == 1: # Só permite que seja respondido caso haja apenas um parâmetro
        sar_base = 1293.20
        calc = how_much/sar_base
        if calc < 2 and calc > 0:
            print(f'Levando em conta a base do salário mínimo R$ {sar_base}',
            f'E o salário informado de {how_much}',
            f'A pessoa ganha {calc} salário mínimo.')
        elif calc > 2:
            print(f'Levando em conta a base do salário mínimo R$ {sar_base}',
            f'E o salário informado de {how_much}',
            f'A pessoa ganha {calc} salários mínimos.')
        else:
            print('Informe um valor válido!')
    else:
        print('Informe apenas um salário!') # Caso exista mais de um parâmetro, ele dirá que está errado e solicitará a função novamente
        calc_sar(*sar)
        
how_much = float(input('Quanto você ganha em salário?'))
calc_sar(how_much)
