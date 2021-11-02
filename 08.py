"""
Faça um programa que pergunte o preço de três produtos e
informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
"""

prod_1 = float(input("Valor do produto 1: R$"))
prod_2 = float(input("Valor do produto 2: R$"))
prod_3 = float(input("Valor do produto 3: R$"))

if prod_1 == prod_2 and prod_1 == prod_3:
    print("Os três produtos tem o mesmo valor!")
elif prod_1 < prod_2 and prod_1 < prod_3:
    print(f"Compre o produto 1! No valor de R${prod_1:.2f}")
elif prod_2 < prod_3:
    print(f"Compre o produto 2! No valor de R${prod_2:.2f}")
else:
    print(f"Compre o produto 3! No valor de R${prod_3:.2f}")