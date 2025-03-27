# 17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

class Converter:
    
    def __init__(self, f):
        self.f = f
        self.c = 5 * (f-32) / 9
    
    @property
    def show_c(self):
        try:
            return self.c
        except Exception as err:
            print(f'Erro: {err}')
    
f = float(input('Informe a temperatura em Fahrenheit a ser convertida; \n'))

conv = Converter(f)

print(f'A temperatura em Fahrenheit é: {f}ºF. \n',
f'A temperatura em Celsius é: {conv.show_c}ºC')
