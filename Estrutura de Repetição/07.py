'''Faça um programa que leia 5 números e informe o maior número.
'''

'''n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
n4 = float(input('Digite um número: '))
n5 = float(input('Digite um número: '))'''




numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um nÃºmero: ")))

MaiorValor = numeros[0]

cont = 1
while cont < len(numeros):
    if numeros[cont] > MaiorValor:
        MaiorValor = numeros[cont]
    cont = cont + 1
        
print ("O maior número é: " + (MaiorValor))