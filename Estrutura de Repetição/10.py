'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

for i in range(n1,n2,1):
    print(i)

if n2 < n1:
    print('Segundo número tem que ser maior que o primeiro')
'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

for i in range(n1 + 1, n2):
        print(i)
for i in range(n2 + 1, n1):
        print(i)