'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))

if dia <= 31 and mes ==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print('Data válida')
elif dia <= 30 and mes==4 or mes==6 or mes==9 or mes==11:
    print('Data válida')
elif dia > 29 and mes == 2:
    print('Data inválida')

else:
    print('Data inválida')
    