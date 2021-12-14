'''Faça um Programa que peça dois números e imprima o maior deles.'''

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n1 > n2:
    print('O maior número entre esses dois é o', n1)
elif n2 > n1:
    print('O maior número entre esses dois é o', n2)
elif n1 == n2:
    print('Os dois números são iguais')
else: 
    print('')