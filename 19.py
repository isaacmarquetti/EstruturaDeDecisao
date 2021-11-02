"""
Faça um Programa que leia um número inteiro menor
que 1000 e imprima a quantidade de centenas, dezenas
e unidades do mesmo.

    Observando os termos no plural a colocação do "e",
    da vírgula entre outros. Exemplo:

    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com:

    326, 300, 100, 320, 310,305, 301, 101, 311,
    111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input("Digite um número entre 1 e 1000: "))

if 0 < num <= 1000:
    if num >= 100:
        centena = num // 100
        dezena = (num % 100) // 10
        unidade = num - (centena * 100 + dezena * 10)
        print(f'{centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')
    elif num >= 10:
        dezena = (num % 100) // 10
        unidade = num - (dezena * 10)
        print(f'{dezena} dezena(s) e {unidade} unidade(s)')
    else:
        print(f'{num} unidade(s)')
else:
    print("Digite um valor válido (entre 1 e 1000")