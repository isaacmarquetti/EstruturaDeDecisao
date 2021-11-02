"""
Faça um Programa que peça um número correspondente
a um determinado ano e em seguida informe se este
ano é ou não bissexto.
"""

ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    if ano % 400 == 0:
        print(f"{ano} é ano bissexto!")
    elif ano % 100 == 0:
        print(f"{ano} não é ano bissexto!")
    else:
        print(f"{ano} é ano bissexto!")
else:
    print(f"{ano} não é ano bissexto!")