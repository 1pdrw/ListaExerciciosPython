'''Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

u = str(input('Nome de usuário: '))
s = str(input('Senha: '))
while u == s:
    print('Erro!')
    u = str(input('Nome de usuário: '))
    s = str(input('Senha: '))
    if u != s:
        print('Usuário: ',u)
        print('Senha: ',s)