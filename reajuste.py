# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

def reajust(num):
    try:
        
        post_reajust = num * 0.05
        
    except Exception as err:
        
        print(f'Aconteceu o seguinte erro: {err} \n',
        'Tente novamente!'
        )
        reajust(num)
    
    return post_reajust


number = float(input('Informe que receberá o reajuste: \n'))

print(reajust(number))
