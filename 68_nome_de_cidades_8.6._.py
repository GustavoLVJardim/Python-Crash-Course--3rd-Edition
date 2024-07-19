"""Nome de cidades: Escreva uma função chamada city_country() que recebe o nome de uma cidade e seu país.
A função deve retornar uma string formatada como esta: "Santiago, Chile".
Chame sua função com pelo menos três pares cidades-país e exiba os valores retornados.
"""

def city_country(city, country):
    return f'{city.title()}, {country.title()}'
     
city_1 = city_country('Goiânia', 'Brasil')
print(city_1)

city_2 = city_country('Covilhã', 'Portugal')
print(city_2)

city_3 = city_country('Miami', 'Estados Unidos')
print(city_3)