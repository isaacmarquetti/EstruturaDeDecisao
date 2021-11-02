"""
Faça um programa que lê as duas notas parciais obtidas
por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece
à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média,
    o conceito correspondente e a mensagem “APROVADO”
    se o conceito for A, B ou C ou “REPROVADO” se o
    conceito for D ou E.
"""

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2

if media < 4.0:
    conceito = 'E'
    situacao = False
elif media < 6.0:
    conceito = 'D'
    situacao = False
elif media < 7.5:
    conceito = 'C'
    situacao = True
elif media < 9.0:
    conceito = 'B'
    situacao = True
else:
    conceito = 'A'
    situacao = True

print(f"Nota 1: {nota1:.1f} ")
print(f"Nota 2: {nota2:.1f} ")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

if situacao:
    print("SITUAÇÃO: APROVADO(A)!")
else:
    print("SITUAÇÃO: REPROVADO(A)!")