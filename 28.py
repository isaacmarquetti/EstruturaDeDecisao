"""
O Hipermercado Tabajara está com uma promoção de carnes
que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá
    levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de
    carne por cliente. Se compra for feita no cartão Tabajara
    o cliente receberá ainda um desconto de 5% sobre o total
    da compra. Escreva um programa que peça o tipo e a
    quantidade de carne comprada pelo usuário e gere um
    cupom fiscal, contendo as informações da compra:

    tipo e quantidade de carne, preço total,
    tipo de pagamento, valor do desconto e valor a pagar.
"""
print("Qual tipo de carne você deseja: ")
print('     OPÇÃO                 Até 5 Kg           Acima de 5 Kg')
print('[1] Filé duplo:      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('[2] Alcatra:         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('[3] Picanha:         R$ 6,90 por Kg          R$ 7,80 por Kg')

tipo = int(input("Digite a opção desejada: "))
peso = float(input("Quantidade de carne (kg): "))

print("Formas de pagamento:")
print('[1] Cartão Tabajara: 5% de desconto')
print('[2] Demais formas: sem desconto')

forma_pag = int(input("Digite a forma de pagamento: "))

tipo_nome = ''
tipo_pag = ''
valor_carne = 0

if tipo == 1:
    tipo_nome = 'Filé Duplo'
    if peso > 5:
        valor_carne = 5.8
    else:
        valor_carne = 4.9
if tipo == 2:
    tipo_nome = 'Alcatra'
    if peso > 5:
        valor_carne = 6.8
    else:
        valor_carne = 5.9
if tipo == 3:
    tipo_nome = 'Picanha'
    if peso > 5:
        valor_carne = 7.8
    else:
        valor_carne = 6.9

subtotal = valor_carne * peso

if forma_pag == 1:
    tipo_pag = 'Cartão Tabajara'
    desconto = 0.05
else:
    tipo_pag = 'Demais forma'
    desconto = 0

valor_desconto = subtotal * desconto
total = subtotal - valor_desconto
print("-------------------")
print("CUPOM FISCAL:")
print("-------------------")
print(f"Tipo de carne: {tipo_nome}")
print(f"Quantidade de carne: {peso}kg")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Tipo de pagamento: {tipo_pag}")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"TOTAL A PAGAR: R${total:.2f}")

