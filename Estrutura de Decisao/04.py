'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

l = str(input('Digite uma letra: '))
if l.isalpha():
    if l == "a":
        print("Essa letra é uma vogal")
    elif l == "e":
        print("Essa letra é uma vogal")
    elif l == "i":
        print("Essa letra é uma vogal")
    elif l == "o":
        print("Essa letra é uma vogal")
    elif l == "u":
        print("Essa letra é uma vogal")
    else:
        print('Essa letra é uma consoante')
