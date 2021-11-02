"""
Faça um Programa que peça um número inteiro e determine
se ele é par ou impar.

Dica: utilize o operador módulo (resto da divisão).
"""
num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')