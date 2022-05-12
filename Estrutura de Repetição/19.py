'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

'''soma=0
numero=[]

quant_num = int(input('Quantos números você quer adicionar? '))
while quant_num != soma:
    num = numero.append(float(input('Digite o numero: ')))

soma += 1

if num > 1000 or num < 0:
    print('Permitido apenas números menores que 1000 e maiores que 0.')


print('Soma do maior e menor: ', max(numero) + min(numero))
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))'''

numero = []
soma = 0

quant_num = int(input("Quantos números você quer adicionar? "))
while quant_num != soma:
    num = float(input("Digite o número: "))

    while num > 1000 or num < 0:
        num = float(input("Digite um número menor que 1000 e maior que 0: "))
        
    numero.append(num)
    soma += 1

print("Maior Valor:",max(numero))
print("Menor valor:",min(numero))
print("Soma do maior e do menor: ", max(numero) + min(numero))