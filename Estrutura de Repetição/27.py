'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''
media = 0
turmas = int(input("Digite quantas turmas tem: "))

for i in range(turmas):
    while True:
        alunos = int(input("Digite quantos alunos tem nas turmas: "))
        if alunos > 40:
            break
    media = ((media * (i - 1)) + alunos) / i
print("A média de alunos por turma é ")

