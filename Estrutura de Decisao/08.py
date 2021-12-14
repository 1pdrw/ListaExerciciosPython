'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('Qual o preço do primeiro produto? '))
p2 = float(input('Qual o preço do próximo produto? '))
p3 = float(input('Qual o preço do último produto? '))

if p1 < p2 and p1 < p3:
    print('Você deve comprar o primeiro produto por ser o mais barato, cujo valor é:', p1)
elif p2 < p1 and p2 < p3:
    print('Você deve comprar o segundo produto por ser o mais barato, cujo valor é:', p2)
elif p3 < p1 and p3 < p2:
    print('Você deve comprar o terceiro produto por ser o mais barato, cujo valor é:', p3)
else:
    print('Os valores dos produtos são iguais')