'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro 
informado pelo usuário.'''

num = int(input("Digite um número: "))
lista = []

for i in range(num):
    if i % 2 == 1:
        lista.append(i)

print("Números primos:", lista)