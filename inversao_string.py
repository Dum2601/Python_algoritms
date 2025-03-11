#**Inversão de String** 🔄: Inverta uma string.

def check_pal(word):
    invert = word[::-1]
    return invert
    
word = input('Qual palavra você deseja inverter? \n')

print(check_pal(word))

