'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

'''numero = int(input("Digite um número: "))

if numero % 2 == 0 and numero != 2:
    print(numero,"não é um número primo.")
else:
    print(numero,"é um número primo.")
'''

num = int(input ("\nDigite um numero inteiro para saber se é primo: "))
cont = 0
div = []

for i in range(num):

    if num%(i+1) == 0:

        cont += 1
        div.append(i+1)

    else:

        cont
        

if cont == 2:

    print ("O numero é primo divisivel por ")

else:

    print ("O numero não é primo pois é divisivel por ",div)