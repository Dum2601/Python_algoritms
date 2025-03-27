# Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

class Sort:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def inverter(self):
        self._list = [self.a, self.b, self.c]
        try:
            self._list.sort(reverse=True)
        except Exception as err:
            print(f'Erro: {err}')
        return self._list
        
    @property
    def show(self):
        return self.inverter()
try:        
    a = int(input('Informe o primeiro número: \n'))
    b = int(input('Informe o segundo número: \n'))
    c = int(input('Informe o terceiro número: \n'))
except Exception as err:
    print(f'Erro: {err}')
sort = Sort(a, b, c)
print(sort.show)
