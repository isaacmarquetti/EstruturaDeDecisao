"""
Faça um programa que calcule as raízes de uma equação
do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e
fazer as consistências, informando ao usuário nas
seguintes situações:

    Se o usuário informar o valor de A igual a zero,
    a equação não é do segundo grau e o programa não
    deve fazer pedir os demais valores, sendo encerrado;

    Se o delta calculado for negativo, a equação não possui
    raizes reais. Informe ao usuário e encerre o programa;

    Se o delta calculado for igual a zero a equação possui
    apenas uma raiz real; informe-a ao usuário;

    Se o delta for positivo, a equação possui duas raiz reais;
    informe-as ao usuário;
"""
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

D = (b**2 - 4*a*c)

if a == 0:
    print("Não é Equação do 2º Grau!")
else:
    if D < 0:
        print("A equação não possui raizes reais.")
    elif D == 0:
        x = (-b / (2 * a))
        print("A equação possui apenas uma raiz.")
        print(x)
    else:
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        print("A equação possui duas raizes.")
        print(f'Raiz 1: {x1}')
        print(f'Raiz 2: {x2}')






