# 21 - Faça um algoritmo que mostre um valor aleatório entre 0 e 100.

import random


def random_number():
    random_value = random.randint(0, 100)
    return random_value
    
print(f'O valor inteiro entre 0 e 100 é: {random_number()}')
