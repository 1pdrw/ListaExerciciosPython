'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

while 1 == 1:
    numero = int(input("Digite um número: "))
    while numero > 16 or numero < 0:
        numero=int(input("Digite um número menor que 16 e maior que 0 por gentileza: "))
    else:             
        fatorial = numero 
        while fatorial > 1:
                fatorial = fatorial - 1
                numero = numero * fatorial
                print (numero)