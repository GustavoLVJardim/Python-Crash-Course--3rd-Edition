"""Pessoa: use um dicionário para armazenar informações sobre uma pessoa que você conhece.
Armazene, o nome, sobrenome, idade e a cidade onde mora. Nomeie as chaves como first_name,
last_name, age e city. Exiba cada informação armazenada em seu dicionário:
"""
#  cria o dicionário pessoa com os pares de chave-valor solicitados:
pessoa = {'first_name' : 'Joyce', 'last_name' : 'Mendes', 'age' : 38, 'city': 'Goiânia'}
#  retorna com a exibição do dicionário:
print(pessoa)

#  optei por percorrer o dicionário com um loop for. Neste loop, percorremos por todos os itens do dicionário
for value in pessoa.items():
    print(value)

#  já neste outro, percorremos apenas os valores que se encontram no dicionário.
for value in pessoa.values():
    print(value)