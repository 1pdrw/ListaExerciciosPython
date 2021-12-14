'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Mais um: '))
n3 = float(input('Outro: '))

if n1 > n2 and n1 > n3:
    print('O maior entre esses 3 números é o', n1)
if n2 > n1 and n2 > n3:
    print('O maior entre esses 3 números é o', n2)
if n3 > n1 and n3 > n2:
    print('O maior entre esses 3 números é o', n3)
else:
    print('Os números são iguais')