# 20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

class Tabuada:
    def __init__(self, num):
        self.num = num
    
    @property
    def show_tab(self):
        try:
            str_tab = ''
            for n in range(1, 11):
                str_tab += f'{n} X {self.num} = {n * self.num}\n'
            return str_tab  
        except Exception as err:
            return f'Erro: {err}'

num = int(input('Informe o número que será usado para a tabuada! \n'))

tabuada = Tabuada(num)
print(tabuada.show_tab)
