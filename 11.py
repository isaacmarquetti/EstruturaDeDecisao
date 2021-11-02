"""
As Organizações Tabajara resolveram dar um aumento
de salário aos seus colaboradores e lhe contraram
para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador
    e o reajuste segundo o seguinte critério, baseado no
    salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%

    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

    salários de R$ 1500,00 em diante : aumento de 5% Após
    o aumento ser realizado, informe na tela:

    o salário antes do reajuste;

    o percentual de aumento aplicado;

    o valor do aumento;

    o novo salário, após o aumento.
"""
salario_atual = float(input("Digite seu salário atual: R$"))

if salario_atual <= 280.0:
    perc = 0.2
elif salario_atual <= 700.0:
    perc = 0.15
elif salario_atual <= 1500.0:
    perc = 0.1
else:
    perc = 0.05

aumento = salario_atual * perc
novo_salario = salario_atual + aumento

print(f'O salário antes do reajuste: R${salario_atual:.2f}')
print(f'O percentual aplicado: {perc * 100:.0f}%')
print(f'O valor do aumento: R${aumento:.2f}')
print(f'O novo salário: R${novo_salario:.2f}')