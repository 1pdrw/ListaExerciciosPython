'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

ate25 = []
ate50 = []
ate75 = []
ate100 = []

while True:
    n = int(input('Digite um número inteiro positivo ou um negativo para parar o programa: '))
    if n >= 0 and n <= 25:
        ate25.append(n)
    elif n >= 26 and n <= 50:
        ate50.append(n)
    elif n >= 51 and n <= 75:
        ate75.append(n)
    elif n >= 76 and n <= 100:
        ate100.append(n)
    elif n < 0:
        break

print('Lista de números no intervalo [0 - 25]: ',ate25)
print('Lista de números no intervalo [26 - 50]: ',ate50)
print('Lista de números no intervalo [51 - 75]: ',ate75)
print('Lista de números no intervalo [76 - 100]: ',ate100)

