'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:'''

'''+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''

salario = float(input('Quanto ganha por hora? '))
horas = int(input('Quantas horas trabalha por mês? '))

salario_bruto = salario * horas
IR = salario_bruto * (11/100)
INSS = salario_bruto * (8/100)
Sindicato = salario_bruto * (5/100)
salario_liquido = (salario_bruto - IR - INSS - Sindicato)

print('Seu salário bruto é de:', salario_bruto, 'reais')
print('Seu IR é de:', IR, 'reais')
print('Seu INSS é de:', INSS, 'reais')
print('Seu sindicato é de:', Sindicato, 'reais')
print('Por fim, seu salário líquido é de:', salario_liquido, 'reais')