'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) 
e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

hotdog = 0
bauru_s = 0
bauru_o = 0
hamb = 0
cheeseb = 0
refri = 0

valorhotdog = hotdog * 1.2
valorbauru_s = bauru_s * 1.2
valorbauru_o = bauru_o * 1.2
valorhamb = hamb * 1.2
valorcheeseb = cheeseb * 1.3
valorrefri = refri * 1




while True:
    cod_prod = int(input('Digite o código do lanche ou -1 para parar de pedir: '))
    quant = int(input('Digite a quantidade que você quer: '))

    if cod_prod == 100:
        hotdog += 1
    elif cod_prod == 101:
        bauru_s += 1
    elif cod_prod == 102:
        bauru_o += 1
    elif cod_prod == 103:
        hamb += 1
    elif cod_prod == 104:
        cheeseb += 1
    elif cod_prod == 105:
        refri += 1
    elif cod_prod == -1:
        break

print('Valor a ser pago pelos Hot Dogs:', valorhotdog)
print('Valor a ser pago pelos Baurus Simples:', valorbauru_s)
print('Valor a ser pago pelos Baurus com Ovo:', valorbauru_o)
print('Valor a ser pago pelos Hamburguers:', valorhamb)
print('Valor a ser pago pelos Cheeseburguers:', valorcheeseb)
print('Valor a ser pago pelos Refrigerantes:', valorrefri)
print('Valor total:', (valorhotdog + valorrefri + valorbauru_o + valorbauru_s + valorhamb + valorcheeseb))