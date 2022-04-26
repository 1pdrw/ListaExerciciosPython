'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

base = int(input("Base: "))
expoente = int(input("Expoente: "))

potencia = 1
contador = 1

while contador <= expoente:
    potencia *= base
    contador +=1

print (base,"elevado a",expoente,"=",potencia)