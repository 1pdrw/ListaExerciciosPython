'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

PA = int(input('Digite a população do país A: '))
PB = int(input('Digite a popula~ção do país B: '))

if PA > PB:
    print('População A já é maior que população B')

    anos = 0
while PA < PB:
    PA = PA + (PA * 0.03)
    PB = PB + (PB * 0.015)
    anos = anos + 1


print (anos,"anos necessários para que a população do país A ultrapasse ou iguale a do país B")

