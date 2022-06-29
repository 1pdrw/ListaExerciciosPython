'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o 
salário inicial do funcionário.'''


ano = 1995
salario = 1000
ano_atual = int(input("Digite em que ano estamos: "))
aumento = 0.015

while (ano >= 1997 and ano <= ano_atual):
    salario = salario * (aumento * 2)
    ano = ano_atual

print(f"O salário em {ano} é de R$ {salario:}")