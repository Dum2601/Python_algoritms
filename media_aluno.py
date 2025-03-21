#  11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 

#  se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

def grade(first, second, third, fourth):
    
    try:
        
        medium = (first + second + third + fourth)/4
    
    except Exception as err:
        
        print(f'Ocorreu o seguinte erro: {err}')
        
    return medium
        
def calc_grade(grade):
    
    try:
        
        if grade > 7:
            
            return True
            
        elif grade < 7:
            
            return False
            
        else:
            print('Valor inválido, tente novamente!')
            calc_grade(grade)
    
    except Exception as err:
            print(f'Ocorreu o seguinte erro: {err}')
            
student_grade_one = float(input('Informe a primeira nota do aluno: \n'))
student_grade_two = float(input('Informe a segunda nota do aluno: \n'))
student_grade_three = float(input('Informe a terceira nota do aluno: \n'))
student_grade_four = float(input('Informe a quarta nota do aluno: \n'))



mediun = grade(first = student_grade_one, second = student_grade_two, third = student_grade_three, fourth = student_grade_four)

if calc_grade(mediun) == True:
    print(f'A nota do aluno foi: {mediun}. \n',
    'Parabéns, ele foi aprovado!')
elif calc_grade(mediun) == False:
    print(f'A nota do aluno foi: {mediun} \n',
    'Infelizmente o aluno foi reprovado!')
