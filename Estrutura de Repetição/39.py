'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo 
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do 
aluno mais baixo, junto com suas alturas.'''

alunos = 10
altura_mais_alto = 72
aluno_mais_alto = 0
altura_mais_baixo = 251
aluno_mais_baixo = 0

for i in range(1, alunos + 1):
    altura = int(input(f"Digite a altura do aluno {i} em cm: "))
    if altura > altura_mais_alto:
        aluno_mais_alto = i
        altura_mais_alto = altura
    if altura < altura_mais_baixo:
        aluno_mais_baixo = i
        altura_mais_baixo = altura

print(f"O aluno mais alto é o aluno {aluno_mais_alto} com {altura_mais_alto} cm")
print(f"O aluno mais baixo é o aluno {aluno_mais_baixo} com {altura_mais_baixo} cm")