salario = float(input("Dgite o salário inicial do funcionário em 1995: "))
ano = 1995
ano_atual = int(input("Digite em que ano estamos: "))
aumento = 0.015

while ano < ano_atual:
    ano = ano_atual
    salario *= 1 + aumento
    aumento += 0.015

print(f"O salário em {ano} é de R$ {salario:}")