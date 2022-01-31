'''Faça um programa que peça uma nota, entre zero e dez.
 Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

n = float(input('Digite uma nota: '))
while n < 0 or n > 10:
        print ("Nota inválida, digite apenas uma nota de 0 a 10.")
        n = float(input("Digite uma nota de 0 a 10: "))

if n > 0 and n < 10:
    print ('Nota:',n)