'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
isto é, considere latas cheias.'''

import math

area = (float)(input("Digite a área em metros quadrados que você deseja pintar: "))
litros = area/6

precolitro = 80
litroslata = 18

precogalao = 25
litrogalao = 3.6

latas = math.ceil(litros / litroslata)
galoes = math.ceil(litros / litrogalao)
total = latas * precolitro
totalg = galoes * precogalao

print('Se você comprar somente latas, o preço será de:', total, 'reais')
print('Se você comprar somente galões, o preço será de:', totalg, 'reais')
print('Se você combinar latas e galões, o preço será:', (litros // litroslata) * precolitro + (math.ceil(((litros % litroslata) / litrogalao)) * precogalao))