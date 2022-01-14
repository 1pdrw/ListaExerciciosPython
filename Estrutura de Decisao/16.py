'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
 O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

import math

a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))


if a == 0:
    print('isso não é uma equação de segundo grau.')
else:  

    delta = b * b - (4*a*c)
    raizdelta0 = -b / (2*a)
    raizdelta = (-b + math.sqrt(delta) ) / (2*a)
    raizdelta2 = (-b - math.sqrt(delta) ) / (2*a)

    if delta < 0:
        print('Equação não possui raízes reais.')
    elif delta == 0:
        print('Apenas uma raiz que é',raizdelta0)
    else:
        print('Duas raízes que são',raizdelta,'e',raizdelta2)
