'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

gen = str(input('Digite (F) para Feminino ou (M) para Masculino ')).upper()

if gen == 'F':
    print('Feminino')
elif gen == 'M':
    print('Masculino')
else:
    print('Sexo inválido.')