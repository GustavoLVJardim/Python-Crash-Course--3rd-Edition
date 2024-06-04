"""Números favoritos: Modifique seu programa do exercício 6.2. para que cada
pessoa possa ter mais de um número favorito. Depois, exiba o nome de cada pessoa
com seus números favoritos:
"""

#  feito o dicionário:
numeros_favoritos = {
    'Gustavo' : ['7'],
    'Joyce' : ['10'],
    'Lis' : ['1'],
    'Kênia' : ['9'],
    'Agnaldo' : ['0'],
}

#  laço for para demonstrar que agora as chaves:nome, possuem como valor: uma lista.
#  com isso, mais números da sorte poderão ser incluídos em cada nome
for number in numeros_favoritos.items():
    print(number)


