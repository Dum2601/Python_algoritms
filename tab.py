def tabuada(i):

    for n in range(1, 11):
        print(f'{i} X {n} = {n*i}')
        
value = int(input('Insira um valor para ser usado na tabuada:'))

tabuada(value)
