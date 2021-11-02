"""
Faça um Programa que leia 2 números e em seguida pergunte
ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado
de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print('ESCOLHA A OPERAÇÃO DESEJADA:')
print('[1] SOMA')
print('[2] SUBTRAÇÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] DIVISÃO')

opcao = int(input('Digite a opção: '))

if opcao == 1:
    result = num1 + num2
elif opcao == 2:
    result = num1 - num2
elif opcao == 3:
    result = num1 * num2
elif opcao == 4:
    result = num1 / num2
else:
    print("Opção inválida!")

print(f'O resultado foi: {result}')

if result % 2 == 0:
    print('O número é par.')
else:
    print("O número é impar.")

if result < 0:
    print('O número é negativo.')
else:
    print('O número é positivo.')

if result == (int(result)):
    print('O valor é inteiro.')
else:
    print('O valor é decimal.')