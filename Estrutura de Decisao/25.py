'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 
 como "Assassino". Caso positivasrário, ele será classificado como "Inocente".
'''
t = str(input('Telefonou para a vítima? '))
l = str(input('Esteve no local do crime? '))
m = str(input('Mora perto da vítima?? '))
d = str(input('Devia para a vítima? '))
t = str(input('Já trabalhou com a vítima? '))

positivas = 0

if t == 'Sim':
    positivas += 1
if l == 'Sim':
    positivas += 1
if m == 'Sim':
    positivas += 1
if d == 'Sim':
    positivas += 1
if t == 'Sim':
    positivas += 1

if positivas == 2:
    print('Suspeito')
elif positivas >= 3 and positivas <= 4:
    print('Cúmplice')
elif positivas == 5:
    print('Assassino')
elif positivas < 2:
    print('Inocente')