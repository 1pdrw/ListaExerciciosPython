'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

n = int(input('Insira um número: '))

if n > 0:
    print('O número que você digitou é positivo')
elif n < 0:
    print('O número que você digitou é negativo')
else: 
    print('Algo incorreto, digite novamente.')