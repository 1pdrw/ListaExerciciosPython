"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""

pares = 0
impares = 0
for i in range(10):
    if int(input("Digite um numero: ")) % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Quantidade de números Pares:", {pares})
print("Quantidade de números Ímpares:", {impares})