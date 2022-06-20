'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é 
jovem, adulta ou idosa, conforme a média calculada.
'''

numero_de_pessoas = int(input("Digite o número de pessoas: "))
media = 0

for i in range(1, numero_de_pessoas + 1):
    idade = int(input("Digite a idade da pessoa {i}: "))
    media = ((media * (i - 1)) + idade) / i

if media < 26:
    print("A turma é jovem, pois a média é",media)
elif media < 60:
    print("A turma é adulta, pois a média é",media)
else:
    print("A turma é idosa, pois a média é",media)