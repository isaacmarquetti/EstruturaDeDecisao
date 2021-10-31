"""
Faça um Programa que leia três números
e mostre o maior e o menor deles.
"""

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

if num1 == num2 and num2 == num3:
    print('Os números são iguais')
elif num1 > num2 and num1 > num3:
    print(f'O maior número é o {num1}!')
    if num2 < num3:
        print(f'O menor número é o {num2}!')
    else:
        print(f'O menor número é o {num3}!')
elif num2 > num3:
    print(f'O maior número é o {num2}!')
    if num1 < num3:
        print(f'O menor número é o {num1}!')
    else:
        print(f'O menor número é o {num3}!')
else:
    print(f'O maior número é o {num3}!')
    if num1 < num2:
        print(f'O menor número é o {num1}!')
    else:
        print(f'O menor número é o {num2}!')