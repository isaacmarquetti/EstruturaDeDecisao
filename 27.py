"""
Uma fruteira está vendendo frutas com a seguinte
tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o
    valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg)
    de morangos e a quantidade (em Kg) de maças adquiridas
    e escreva o valor a ser pago pelo cliente.
"""

morango_kg = float(input("Quantos kg de morango você deseja? "))
maca_kg = float(input("Quantos kg de maça você deseja? "))

if morango_kg >= 5:
    morango_v = 2.2
else:
    morango_v = 2.5

if maca_kg >= 5:
    maca_v = 1.5
else:
    maca_v = 1.8

frutas_kg = morango_kg + maca_kg
frutas_v = (maca_v * maca_kg) + (morango_v * morango_kg)

desconto = 0

if frutas_kg >= 8 or frutas_v >= 25.0:
    desconto = 0.1

total = frutas_v - (frutas_v * desconto)

print("Você comprou:")
print(f"Morango: {morango_kg}kg | Valor: R${morango_v:.2f}")
print(f"Maça: {maca_kg}kg | Valor: R${maca_v:.2f}")
print(f"Valor: R${frutas_v:.2f} | {frutas_kg}kg ")
print(f'Valor com desconto: R${total:.2f}')