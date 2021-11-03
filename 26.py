"""
Um posto está vendendo combustíveis com a seguinte tabela
de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro

    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma:
    A-álcool, G-gasolina), calcule e imprima o valor
    a ser pago pelo cliente sabendo-se que o preço do
    litro da gasolina é R$ 2,50 o preço do litro do álcool
    é R$ 1,90.
"""
print("----------------------------------------------")
print("             POSTO DE COMBUSTÍVEL")
print("----------------------------------------------")
print("Gasolina: R$ 2,50")
print("Álcool: R$ 1,90")
print("----------------------------------------------")

litros = float(input("Quantos litros de combustível? "))
print("Escolha o tipo:  [A] Álcool  [G] Gasolina")

comb = input("Qual tipo de combustível? ").lower()

valor = desconto = 0
gasolina = 2.5
alcool = 1.9
tipo = ''

if comb == 'a':
    tipo = 'Álcool'
    valor = litros * alcool
    if litros < 20:
        desconto = (alcool * 0.03) * litros
    else:
        desconto = (alcool * 0.05) * litros

if comb == 'g':
    tipo = 'Gasolina'
    valor = litros * gasolina
    if litros < 20:
        desconto = (gasolina * 0.04) * litros
    else:
        desconto = (gasolina * 0.06) * litros

total = valor - desconto

print(f"Litros vendidos: {litros} litros")
print(f"Tipo de combustível: {tipo}")
print(f"Valor sem desconto: R${valor:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"VALOR A SER PAGO: R${total:.2f}")
