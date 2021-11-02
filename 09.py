"""
Faça um Programa que leia três números e mostre-os
em ordem decrescente.
"""
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f'A ordem é: {num1}, {num2} e {num3}')
    else:
        print(f'A ordem é: {num1}, {num3} e {num2}')

elif num2 >= num3:
    if num1 >= num3:
        print(f'A ordem é: {num2}, {num1} e {num3}')
    else:
        print(f'A ordem é: {num2}, {num3} e {num1}')
else:
    if num1 >= num2:
        print(f'A ordem é: {num3}, {num1} e {num2}')
    else:
        print(f'A ordem é: {num3}, {num2} e {num1}')
