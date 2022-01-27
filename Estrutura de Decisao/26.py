'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
 litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

'''

l = int(input('Quantos litros comprados? '))
t = str(input('Tipo do Combustível? A - Alcool G - Gasolina '))

if t == 'A':
    preco = 1.90
elif t == 'G':
    preco = 2.50

if t == 'A' and l <= 20:
    print('O valor pago por',l,'litros é',(preco * l * 3)/100,'reais.')