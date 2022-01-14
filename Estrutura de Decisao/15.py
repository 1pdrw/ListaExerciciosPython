'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

l1 = float(input('Qual valor do primeiro lado? '))
l2 = float(input('Qual valor do segundo lado? '))
l3 = float(input('Qual valor do terceiro lado? '))

if l1 + l2 < l3:
    print('Isso não é um triângulo')
elif l1 + l3 < l2:
    print('Isso não é um triângulo')
elif l2 + l3 < l1:
    print('Isso não é um triângulo')

elif l1 == l2 == l3:
    print('Triângulo Equilátero')
elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
    print('Triângulo Isósceles')
elif l1 != l2 != l3:
    print('Triangulo Escaleno')