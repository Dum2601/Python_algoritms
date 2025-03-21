#**Inversão de String** 🔄: Inverta uma string.

class Invert:
    def __init__(self, word):
        self.word = word
    
    def invert_str(self):
        try:
            return self.word[::-1]
        except Exception as err:
            print(f'Erro: {err}')
            

word = str(input('Informe a String a ser invertida: \n'))

invert = Invert(word)

print(invert.invert_str())
