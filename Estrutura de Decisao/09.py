'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um: '))
n3 = float(input('Digite outro: '))

if n1 > n2 > n3:
    print('Ordem decrescente:', n1,'-', n2,'-', n3)
elif n1 > n3 > n2:
    print('Ordem decrescente:', n1,'-', n3,'-', n2)
elif n2 > n1 > n3:
    print('Ordem decrescente:', n2,'-', n1,'-', n3)
elif n2 > n3 > n1:
    print('Ordem decrescente:', n2,'-', n3,'-', n1)
elif n3 > n2 > n1:
    print('Ordem decrescente:', n3,'-', n2,'-', n1)
elif n3 > n1 > n2:
    print('Ordem decrescente:', n3,'-', n1,'-', n2)
elif n1 == n2 == n3:
    print('Os números são iguais')