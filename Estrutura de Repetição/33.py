'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''

quant_temp = int(input('Digite quantas temperaturas o departamento quer comparar: '))

for i in range(quant_temp):
    temp = int(input('Quantos graus tá medindo cada temperatura? '))

    print('A maior temperatura informada foi de',max(temp),'graus.')
    print('A menor temperatura informada foi de',min(temp),'graus.')
    print('A média das temperaturas informadas foi de',(sum(temp) / quant_temp),'graus.')