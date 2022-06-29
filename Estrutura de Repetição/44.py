'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''

jose = 0
joao = 0
pedro = 0
robson = 0
nulo = 0
votobranco = 0
voto = 0

print("Candidatos         Código  "
           "\n-------------------------"
           "\nJosé             |    1"
           "\nJoão             |    2"
           "\nPedro            |    3"
           "\nRobson           |    4"
           "\n"
     "\nOpções adicionais"
           "\n-------------------------"
           "\nVoto nulo        |    5"
           "\nVoto em Branco   |    6"
           "\nSair da votação  |    7")
print('')
print('')
print('')
while voto != 7:
    voto = int(input('Digite aqui seu voto: '))
    if voto == 1:
        print('Você votou em José')
        jose += 1
    elif voto == 2:
        print('Você votou em João')
        joao += 1
    elif voto == 3:
        print('Você votou em Pedro')
        pedro += 1
    elif voto == 4:
        print('Você votou em Robson')
        robson += 1
    elif voto == 5:
        print('Você votou nulo')
        nulo += 1
    elif voto == 6:
        print('Você votou branco')
        votobranco += 1

print('José obteve',jose,'votos.')
print('João obteve',joao,'votos.')
print('Pedro obteve',pedro,'votos.')
print('Robson obteve',robson,'votos.')
print(nulo,'pessoas votaram nulo.')
print(votobranco,'pessoas votaram branco.')