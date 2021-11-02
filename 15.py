"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem
ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma
    de quaisquer dois lados for maior que o terceiro;

    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

l1 = int(input("Digite o valor do 1º lado: "))
l2 = int(input("Digite o valor do 2º lado: "))
l3 = int(input("Digite o valor do 3º lado: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("É um TRIÂNGULO EQUILÁTERO!")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("É um TRIÂNGULO ESCALENO!")
    else:
        print("É UM TRIÂNGULO ISÓSCELES!")
else:
    print("Os valores não formam um triângulo!")