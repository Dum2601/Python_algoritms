# 20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

class Tab:
    def __init__(self, x):
        self.x = x
        
    def create_tab(self):
        for i in range(1, 11):
            print(f'{i} * {self.x} = {i*self.x}')
            

number = int(input('Informe o número desejado: \n'))

tab = Tab(number)

tab.create_tab()
