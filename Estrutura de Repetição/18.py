'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

soma = 0
numero = []

quant_num = int(input('Quantos números você quer adicionar? '))
while quant_num != soma:
    num = numero.append(float(input('Digite o numero: ')))
    soma += 1

print('Soma do maior e menor: ', max(numero) + min(numero))
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))