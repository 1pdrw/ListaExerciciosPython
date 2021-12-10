'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

salario = int(input('Quanto você recebe por hora trabalhada? '))
horas = int(input('Quantas horas você trabalha por dia? '))
dias = int(input('Digite aqui quantos dias tem o mês que você deseja calcular: '))

if dias == 30:
    print('Em abril, junho, setembro e novembro você recebe', salario * (horas * dias), 'reais')
elif dias == 31:
    print('Em janeiro, março, maio, julho, agosto, outubro e dezembro você recebe', salario * (horas * dias), 'reais')
elif dias == 29:
    print('Em fevereiro nesse ano bissexto você recebe', salario *(horas * dias), 'reais')
elif dias == 28:
    print('Em fevereiro você recebe', salario *(horas * dias), 'reais')
else:
    print('Essa quantidade de dias não corresponde a um mês')