# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

class Value:
    def __init__(self, x):
        self.x = x
        
    
    def percent(self):
        self._percent_value = self.x * 0.05
        return self._percent_value
        
    @property
    def show_value(self):
        price_reajusted = self.x + self.percent()
        return price_reajusted
        
try:        
    number = float(input('Qual o valor a ser calculado?\n'))
except Exception as err:
    print(f'Erro ao declarar o valor a ser recebido!\n',
    f'Erro: {err}')

try:
    value = Value(number)
except Exception as err:
    print('Erro ao tentar instanciar a classe!\n',
    f'Erro: {err}')

print(value.show_value)
