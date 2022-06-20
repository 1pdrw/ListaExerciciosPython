'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = str(input("Nome: "))
while (len(nome) <=   3 ):
	nome = str(input("Nome: "))

idade = int(input("Idade: "))
while ( idade > 150 or idade < 0 ):
	idade = int(input("Idade: "))
	
	
salario = float(input("Salário: "))
while (salario < 0 ):
	salario = float(input("Salário: "))
	

sexo = str(input("Sexo: (M/F) "))
while  sexo != "f" and sexo != "m" :
	sexo = str(input("Sexo: (M/F) "))
	

estado_civil = str(input("Estado Civil: "))
while (estado_civil !=  "s" and estado_civil !=  "c" and estado_civil !=  "v" and estado_civil !=  "d" ):
	estado_civil = str(input("Estado Civil: "))     

print('Nome:',nome)
print('Idade:',idade)
print('Salário:',salario)
print('Sexo: ',sexo)
print('Estado Civil:',estado_civil)
