'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada 
questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido 
informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.'''

continuar = ''
erro = 0
acerto = 0
aluno = str(input('Digite o nome do aluno: '))

while continuar not in 'não' or continuar not in 'nao':
    for i in range(1,11):
        print('Questão',i )
    questao = str.upper(input('Digite a resposta: '))
    if i == 1:
        if questao != 'A':
            erro += 1
        else:
            acerto += 1
    elif i == 2:
        if questao != 'B':
            erro += 1
        else:
            acerto += 1
    elif i == 3:
        if questao != 'C':
            erro += 1
        else:
            acerto += 1
    elif i == 4:
        if questao != 'D':
            erro += 1
        else:
            acerto += 1
    elif i == 5:
        if questao != 'E':
            erro += 1
        else:
            acerto += 1
    elif i == 6:
        if questao != 'E':
            erro += 1
        else:
            acerto += 1
    elif i == 7:
        if questao != 'D':
            erro += 1
        else:
            acerto += 1
    elif i == 8:
        if questao != 'C':
            erro += 1
        else:
            acerto += 1
    elif i == 9:
        if questao != 'B':
            erro += 1
        else:
            acerto += 1
    elif i == 10:
        if questao != 'A':
            erro += 1
        else:
            acerto += 1

    print(aluno,'acertou',acerto,'questões.')
print(aluno,'errou',erro,'questões.')
continuar = str(input('Outro aluno irá usar o sistema? '))
