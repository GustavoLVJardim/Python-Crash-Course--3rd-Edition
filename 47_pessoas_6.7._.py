"""Pessoas: Comece com o programa escrito para o exercício 6.1.. Crie dois
dicionários novos representando pessoas diferentes e armazene todos os três
dicionários em uma lista chamada people. Percorra a sua lista de pessoas
com um loop. À medida que percorre a lista, exiba tudo o que sabe sobre cada pessoa.
"""

#  cria os três dicionários de pessoas com os pares de chave-valor:
pessoa_1 = {'first_name' : 'Joyce', 'last_name' : 'Mendes', 'age' : 38, 'city': 'Goiânia'}
pessoa_2 = {'first_name' : 'Gustavo', 'last_name' : 'Jardim', 'age': 35, 'city' : 'Pires do Rio'}
pessoa_3= {'first_name' : 'Lis', 'last_name' : 'Jardim', 'age' : 8, 'city' : 'Goiânia'}

#  cria a lista people:
people = [pessoa_1, pessoa_2, pessoa_3]

#  Neste loop percorremos por todos os itens dos três dicionários:
for person in people:
    print(people)
