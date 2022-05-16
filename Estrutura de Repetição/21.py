'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(numero,"não é um número primo.")
if numero == 2:
    print(numero,"é o único número primo par existente.")
else:
    print(numero,"é um número primo.")
