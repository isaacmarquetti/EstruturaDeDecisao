"""
Faça um programa que faça 5 perguntas para uma pessoa
sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

    O programa deve no final emitir uma classificação sobre
    a participação da pessoa no crime. Se a pessoa responder
    positivamente a 2 questões ela deve ser classificada como
    "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
    "Assassino". Caso contrário, ele será classificado
    como "Inocente".
"""

print("----------------------------------")
print("PERGUNTAS SOBRE O CRIME: (SIM/NÃO)")
print("----------------------------------")
p1 = input("Telefonou para a vítima? ").lower()
p2 = input("Esteve no local do crime? ").lower()
p3 = input("Mora perto da vítima? ").lower()
p4 = input("Devia para a vítima? ").lower()
p5 = input("Já trabalhou com a vítima? ").lower()

resp_sim = 0

if p1 == 'sim':
    resp_sim += 1
if p2 == 'sim':
    resp_sim += 1
if p3 == 'sim':
    resp_sim += 1
if p4 == 'sim':
    resp_sim += 1
if p5 == 'sim':
    resp_sim += 1

if resp_sim >= 5:
    print('Classificação: ASSASSINO!')
elif resp_sim >= 3:
    print('Classificação: Cúmplice!')
elif resp_sim >= 2:
    print('Classificação: Suspeita!')
else:
    print("Classificação: Inocente!")


