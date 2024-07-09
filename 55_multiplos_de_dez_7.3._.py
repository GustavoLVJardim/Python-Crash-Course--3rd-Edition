"""Múltiplos de dez: Solicite ao usuário um número e informe se o número
é múltiplo de 10 ou não.
"""

number = input("Me dê um número, por favor: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} é um múltiplo de 10.")
else:
    print(f"{number} não é um múltiplo de 10.")