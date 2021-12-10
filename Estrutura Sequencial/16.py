'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

import math

area = (float)(input("Digite a área em metros quadrados que você deseja pintar: "))
litros = area/3

precolitro = 80.0
litroslata = 18

latas = math.ceil(litros / litroslata)
total = latas * precolitro

print ('Você usará ',latas,'latas de tinta')
print ('O preco total é de: R$',total)
