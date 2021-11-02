"""
Faça um Programa que peça uma data no formato
dd/mm/aaaa e determine se a mesma é uma data válida.
"""

data = input('Digite uma data no formato (dd/mm/aaaa): ').split('/')

dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if ano > 0 and ano % 4 == 0:
    if ano % 400 == 0:
        if mes == 2:
            if 1 <= dia <= 29:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if 1 <= dia <= 31:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')
        elif mes in (4, 6, 9, 11):
            if 1 <= dia <= 30:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')

    elif ano % 100 == 0:
        if mes == 2:
            if 1 <= dia <= 28:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if 1 <= dia <= 31:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')
        elif mes in (4, 6, 9, 11):
            if 1 <= dia <= 30:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')

    else:
        if mes == 2:
            if 1 <= dia <= 29:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if 1 <= dia <= 31:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')
        elif mes in (4, 6, 9, 11):
            if 1 <= dia <= 30:
                print(f'{dia}/{mes}/{ano} é uma data válida!')
            else:
                print(f'{dia}/{mes}/{ano} não é uma data válida!')

else:
    if mes == 2:
        if 1 <= dia <= 28:
            print(f'{dia}/{mes}/{ano} é uma data válida!')
        else:
            print(f'{dia}/{mes}/{ano} não é uma data válida!')
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= dia <= 31:
            print(f'{dia}/{mes}/{ano} é uma data válida!')
        else:
            print(f'{dia}/{mes}/{ano} não é uma data válida!')
    elif mes in (4, 6, 9, 11):
        if 1 <= dia <= 30:
            print(f'{dia}/{mes}/{ano} é uma data válida!')
        else:
            print(f'{dia}/{mes}/{ano} não é uma data válida!')
