# 11. **Palíndromo** 🔁: Verifique se uma string é um palíndromo.

def pal_check(word):
    inverted_name = word[::-1]
    if inverted_name == word:
        print('A palavra é um palíndromo!')
    elif inverted_name != word:
        print('A palavra não é um palíndromo!')
    else:
        print('Informe uma palavra válida!')
        pal_check(word)

name = input('Informe a palavra: \n')

pal_check(name)