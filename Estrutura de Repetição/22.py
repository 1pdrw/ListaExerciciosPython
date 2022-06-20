'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
'''


num = int(input ("\nDigite um numero inteiro para saber se é primo: "))
cont = 0
div = []

for i in range(num):

    if num % (i + 1) == 0:

        cont += 1
        div.append(i + 1)

    else:

        cont
        

if cont == 2:
    print ("O numero é primo.")
else:
    print ("O numero não é primo e é divisível por:",div)
