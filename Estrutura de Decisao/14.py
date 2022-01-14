'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou
 “REPROVADO” se o conceito for D ou E.'''

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
media = (n1 + n2) / 2

if media >= 4 and media <= 6:
    print('Nota: ',n1)
    print('Nota 2: ',n2)
    print('Conceito: D')
    print('Média: ',media)
    print('Reprovado.')

elif media >= 0 and media <= 4:
    print('Nota: ',n1)
    print('Nota 2: ',n2)
    print('Conceito: E')
    print('Média: ',media)
    print('Reprovado.')

elif media >= 6 and media <= 7.5:
    print('Nota: ',n1)
    print('Nota 2: ',n2)
    print('Conceito: C')
    print('Média: ',media)
    print('Aprovado.')

elif media >= 7.5 and media <= 9:
    print('Nota: ',n1)
    print('Nota 2: ',n2)
    print('Conceito: B')
    print('Média: ',media)
    print('Aprovado.')

elif media >= 9 and media <= 10:
    print('Nota: ',n1)
    print('Nota 2: ',n2)
    print('Conceito: A')
    print('Média: ',media)
    print('Aprovado.')