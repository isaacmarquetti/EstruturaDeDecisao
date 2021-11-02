"""
Faça um Programa que peça um número e informe se o
número é inteiro ou decimal.

Dica: utilize uma função de arredondamento.
"""
import math

num = float(input("Digite um número inteiro ou decimal: "))

num_teste = num - math.floor(num)

if num_teste == 0:
    print('É um número inteiro.')
else:
    print('É um número decimal.')