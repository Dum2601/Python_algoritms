# 11. **Palíndromo** 🔁: Verifique se uma string é um palíndromo.

class Palindromo:
    
    def __init__(self, word):
        self.word = word
    
    def pal_check(self):
        try:
            inverted_name = self.word[::-1]
        except Exception as err:
            print(f'Erro: {err}')
        
        try:    
            if inverted_name == self.word:
                print('A palavra é um palíndromo!')
            elif inverted_name != self.word:
                print('A palavra não é um palíndromo!')
            else:
                print('Informe uma palavra válida!')
                pal_check(self.word)
        except Exception as err:
            print(f'Erro: {err}')

name = input('Informe a palavra: \n')

palindromo = Palindromo(name)

palindromo.pal_check()
