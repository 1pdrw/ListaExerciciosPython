'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

n = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))

op = int(input('Qual operação deseja realizar? 1 - Adição 2 - Subtração 3 - Multiplicação 4 - Divisão'))


if op == 1:
   res = n + n2
elif op == 2:
   res = n - n2
elif op == 3:
   res = n * n2
elif op == 4:
   res = n / n2

if res % 2 == 0:
    print('Par')
elif res % 1 == 0:
    print('Inteiro')
elif res > 0:
    print('Positivo')
else:
    print('Ímpar')
    print('Decimal')
    print('Negativo')
