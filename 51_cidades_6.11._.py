"""Cidades: Crie um dicionário chamado cities. Utilize o nome de três cidades
como chaves de seu dicionário. Crie um dicionário de informações sobre cada
cidade e inclua o país em que a cidade está, sua população aproximada e um fato
sobre essa cidade. O nome das chaves para o dicionário de cada cidade devem ser
alguma coisa como country, population e fact. Exiba o nome de cada cidade e todas
as informações que você armazenou a respeito.
"""

def main():
    cities = {
        'Covilhã': {'Country': 'Portugal', 'Fact': 'Castelo Branco', 'Population': 47000 },
        'Goiânia': {'Country': 'Brasil', 'Fact': 'Goias', 'Population': 1500000},
        'Miami': {'Country': 'Estados Unidos', 'Fact': 'Flórida', 'Population': 440000},
    }
    
    for k, v in cities.items():
        print(f" About the city {k}: {v}")



def cities():
    return


main()