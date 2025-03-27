#  11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 

#  se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

class Student:
    def _init_(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def grade_calc(self):
        self._list_grade = [self.a, self.b, self.c, self.d]
        try:
            self._mediun = sum(self._list_grade) / len(self._list_grade)
        except Exception as err:
            print('Erro no método grade_calc da classe Student.\n',
            f'Erro: {err}')
        return self._mediun
    
    @property
    def status(self):
        try:
            if self.grade_calc() >= 7:
                return True
            elif self.grade_calc() < 7:
                return False
        except Exception as err:
            print('Erro no método status da classe Student.\n',
            f'Erro: {err}')
        
    @property
    def grade(self):
        return self.grade_calc()
        


a = float(input('Qual a primeira nota do aluno?\n'))        
b = float(input('Qual a segunda nota do aluno?\n'))
c = float(input('Qual a terceira nota do aluno?\n'))
d = float(input('Qual a quarta nota do aluno?\n'))


student = Student(a, b, c, d)

try:
    if student.status == True:
        print(f'A média do aluno é {student.grade}.',
        f'\nO aluno foi aprovado!')
    elif student.status == False:
        print(f'A média do aluno é {student.grade}.',
        f'\nO aluno foi Reprovado!')
except Exception as err:
    print('Erro no nos ifs na respo
