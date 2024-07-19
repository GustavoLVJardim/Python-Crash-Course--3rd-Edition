"""Descreva uma função chama describe_city() que aceite o nome de uma cidade e de seu país.
A função deve exibir uma simples frase, como Reykjavik fica na Islândia. Forneça ao parâmetro
do país um valor default. Chame sua função para três cidades diferentes e, pelo menos,
para uma que não esteja no país default
"""

def describe_city(city_1, city_2, city_3, country='Brasil'):
    print(f'{city_1}, {city_2} e {city_3} são cidades que ficam no {country}.')



describe_city('Goiânia', 'Aracajú', 'Fundão')


