"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f'O número {num1} é maior que {num2}.')
elif num1 < num2:
    print(f'O número {num2} é maior que {num1}.')
else:
    print(f'os números são iguais.')
