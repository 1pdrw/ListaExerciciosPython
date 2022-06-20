'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

'''numero = int(input("Digite um número: "))

if numero % 2 == 0 and numero != 2:
    print(numero,"não é um número primo.")
else:
    print(numero,"é um número primo.")
'''

num = int(input("Digite um número: "))
contador = 1
while contador <= num:
    if num % 2 == 1:
        contador=contador+1
        print(num,'é um número primo.')
    else:
        print(num,'não é um número primo.')