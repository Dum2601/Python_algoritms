# # 17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

class Converter:
    def __init__(self, c):
        self.c = c
    
    def celsius(self):
        try:
            return 5 * (f-32) / 9
        except Exception as err:
            print(f'Erro: {err}')

f = float(input('Informe a temperatura em farenheit: \n'))

converter = Converter(f)



print(converter.celsius())
        
        
