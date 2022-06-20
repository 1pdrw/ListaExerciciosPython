'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o 
valor para em cada um.
'''

quant_CD = int(input("Digite a quantidade de CDs: "))

cds = 0
valor = 0

for x in range(quant_CD):
	valorCD = eval(input("Digite o valor do CD: "))
	valor = valor + valorCD
	valorMedio = valor / quant_CD
	cds += 1

print("O valor total gasto: R$", valor)
print("O valor médio gasto por cada CD foi de: R$", valorMedio)