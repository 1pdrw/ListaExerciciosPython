'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho = float(input('Qual o tamanho em MB do seu arquivo? '))
velo = float(input('Qual a velocidade da sua internet em mbps? '))

tempodown = (tamanho / velo) / 60
print('O tempo de download do seu arquivo será de', tempodown, 'minutos')