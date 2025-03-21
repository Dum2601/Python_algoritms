from random import randint

def check_random(a):
    try:
        random_num = randint(0, 9)  
        if a == random_num:
            return True, random_num 
        else:
            return False, random_num  
    except Exception as err:
        print(f'Ocorreu o seguinte erro: {err}')
        return False, None  

def game():
    try:
        player_number = int(input('Informe um número para iniciar o jogo (entre 0 e 9): \n'))
        if player_number < 0 or player_number > 9:
            print("Número inválido! Escolha um número entre 0 e 9.")
            return  
        

        result, random_num = check_random(player_number)
        
        if result:
            print(f'Número escolhido pelo jogador: {player_number}. \nNúmero escolhido pela máquina: {random_num}. \nO jogador venceu! \n')
        else:
            print(f'Número escolhido pelo jogador: {player_number}. \nNúmero escolhido pela máquina: {random_num}. \nO jogador perdeu! \n')
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
    
    except Exception as err:
        print(f'Erro: {err}')


game()

while True:
    again = input('Deseja jogar novamente? (s/n): ').lower()
    if again == 's':
        game()
    elif again == 'n':
        print('Jogo encerrado!')
        break
    else:
        print('Opção inválida, por favor, escolha "s" para sim ou "n" para não.')
