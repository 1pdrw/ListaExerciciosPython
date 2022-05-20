'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

c1 = 0
c2 = 0
c3 = 0
eleitores = int(input("Qual o número total de eleitores? "))

for x in range(eleitores):
    voto = int(input("Em que candidato você quer votar? Candidato A = 1 // Candidato B = 2 // Candidato C = 3 "))
    if (voto == 1):
        c1 = c1 + 1
    elif (voto == 2):
        c2 = c2 + 1
    elif (voto == 3):
        c3 = c3 + 1
    else:
        print("Voto inválido")

print('O candidato 1 teve o total de',c1,'votos.')
print('O candidato 2 teve o total de',c2,'votos.')
print('O candidato 3 teve o total de',c3,'votos.')

