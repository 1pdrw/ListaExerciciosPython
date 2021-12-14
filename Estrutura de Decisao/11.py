'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

s = float(input('Digite seu salário: '))
v = (20 * s) / 100
v2 = (15 * s) / 100
v3 = (10 * s) / 100
v4 = (5 * s) / 100

if s <= 280:
    print('Seu salário é de', s, 'R$')
    print('Seu aumento em % foi de 20%')
    print('Seu aumento foi de', v, 'reais')
    print('Seu novo salário após o aumento é de', s + v)

elif s <= 700 and s >= 280:
    print('Seu salário é de', s, 'R$')
    print('Seu aumento em % foi de 15%')
    print('Seu aumento foi de', v2, 'reais')
    print('Seu novo salário após o aumento é de', s + v2)

elif s >= 700 and s <= 1500:
    print('Seu salário é de', s, 'R$')
    print('Seu aumento em % foi de 15%')
    print('Seu aumento foi de', v3, 'reais')
    print('Seu novo salário após o aumento é de', s + v3)

else:
    print('Seu salário é de', s, 'R$')
    print('Seu aumento em % foi de 15%')
    print('Seu aumento foi de', v4, 'reais')
    print('Seu novo salário após o aumento é de', s + v4)


