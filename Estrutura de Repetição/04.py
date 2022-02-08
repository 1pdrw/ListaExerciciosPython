'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa 
que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

PA = 80000
PB = 200000

anos = 0
while PA < PB:
    PA = PA + (PA * 0.03)
    PB = PB + (PB * 0.015)
    anos = anos + 1

print (anos,"anos necessários para que a população do país A ultrapasse ou iguale a do país B")