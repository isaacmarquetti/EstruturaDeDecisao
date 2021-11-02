"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima
    na tela as informações, dispostas conforme o exemplo
    abaixo. No exemplo o valor da hora é 5 e a quantidade
    de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("Valor da sua hora trabalhada: R$"))
horas_trab = float(input("Horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trab

if salario_bruto <= 900.0:
    ir = 0
elif salario_bruto <= 1500.0:
    ir = 0.05
elif salario_bruto <= 2500.0:
    ir = 0.1
else:
    ir = 0.2

imposto_renda = salario_bruto * ir
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
descontos = imposto_renda + inss
salario_liq = salario_bruto - descontos

print(f'Salário Bruto:     R${salario_bruto:.2f}')
print(f'(-) IR ({ir * 100:.0f}%):       R${imposto_renda:.2f}')
print(f'(-) INSS (10%):    R${inss:.2f}')
print(f'FGTS (11%):        R${fgts:.2f}')
print(f'Total descontos:   R${descontos:.2f}')
print(f'Salário Líquido:   R${salario_liq:.2f}')
