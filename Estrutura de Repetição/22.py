'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
'''

'''numero = int(input("Digite um número inteiro: "))
primo = True
if numero % 2 == 0 and numero != 2:
    primo = False
    print(numero,"não é primo!")
if primo:
    print(numero,"é primo!")    '''

numero = int(input("Digite um número inteiro: "))
for i in range(2,numero):
    print(i)