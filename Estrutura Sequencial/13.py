'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

gen = str(input('Qual seu gênero sexual? '))
alt = float(input('Digite sua altura para que eu possa calcular seu peso ideal: '))

if gen == 'Feminino':
    print('Seu peso ideal seria', (62.1*alt) - 44.7, 'kg')

if gen == 'Masculino':
    print('Seu peso ideal seria:', (72.7*alt) - 58, 'kg')