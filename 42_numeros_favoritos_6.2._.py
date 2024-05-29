"""Números favoritos: Use um dicionário para armazenar os números favoritos das pessoas.
Pense em cinco nomes e os utilize como chaves em seu dicionário. Pense em um número
favorito para cada pessoa e armazene cada um como um valor em seu dicionário. Exiba o nome
de cada pessoa e seu número favorito. Para que tudo fique ainda mais divertido, pergunte a
alguns amigos e obtenha alguns dados reais para o seu programa:
"""
#  feito o dicionário:
numeros_favoritos = {
    'Gustavo' : 7,
    'Joyce' : 10,
    'Lis' : 1,
    'Kênia' : 9,
    'Agnaldo' : 0,
}

#  laço for para iterar com cada item (pares de chave-valor) do dicinário
for k, v in numeros_favoritos.items():
    print(f'{k} tem o número favorito como: {v}')  # retorna com cada nome e número favorito, por f-strings