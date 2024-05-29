"""Números ordinais: Os números ordinais designam sua posição em uma lista, como 1º ou 2º.
Em inglês, 1st ou 2nd. A maioria dos números ordinais em inglês termina em th, exceto 1, 2 e 3.
- armazene os números de 1 a 9 em uma lista;
- percorra com um loop toda a lista;
- use uma sequência if-elif-else dentro do loop para exibir a terminação ordinal adequada para cada número.
Sua saída deve ler: "1st 2nd 3rd 4th 5th 6th 7th 8th 9th" e cada resultado deve estar em uma lista separada:
"""
#  armazene os números de 1 a 9 em uma lista:
positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(positions)

for position in positions:
    if position == 1:
        print("1st")
    elif position == 2:
        print("2nd")
    elif position == 3:
        print("3rd")
    else:
        print(f"{position}th")




