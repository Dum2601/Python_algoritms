# **Inversão de String** 🔄: Inverta uma string.

def invert_string(word):
    invert = word[::-1]
    return invert
    
word = input('Qual palavra você deseja inverter? \n')

print(invert_string(word))

