"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de
notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais,
    o programa fornece duas notas de 100, uma nota de 50,
    uma nota de 5 e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais,
    o programa fornece três notas de 100, uma nota de 50,
    quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

valor = int(input("Digite o valor que quer sacar: (MIN:10/MAX:600) R$"))

if 10 < valor < 600:
    cem = valor // 100
    cinquenta = (valor - (cem * 100)) // 50
    dez = (valor - ((cem * 100) + (cinquenta * 50))) // 10
    cinco = (valor - ((cem * 100) + (cinquenta * 50) + (dez * 10))) // 5
    um = (valor - ((cem * 100) + (cinquenta * 50) + (dez * 10) + (cinco * 5)))
    print("CAIXA ELETRÔNICO:")
    print(f' NOTA DE 100: {cem}')
    print(f' NOTA DE 50: {cinquenta}')
    print(f' NOTA DE 10: {dez}')
    print(f' NOTA DE 5: {cinco}')
    print(f' NOTA DE 1: {um}')

else:
    print("Valor não dispónivel para saque.")