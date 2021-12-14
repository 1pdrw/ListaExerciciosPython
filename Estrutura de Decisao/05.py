'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

n1 = float(input('Digite a nota parcial da sua prova 1: '))
n2 = float(input('Digite a nota parcial da sua prova 2: '))

med = (n1 + n2) / 2

if med >= 7 and med < 10:
    print('Você foi aprovado!')
elif med < 7:
    print('Você foi reprovado!')
elif med == 10:
    print('Você foi aprovado com distinção. Parabéns!')
