"""Carros: Crie uma função que armazene informações sobre um carro em um dicionário. A função deve
sempre receber um fabricante e um nome de modelo. Em seguida, deve aceitar um número arbitrário de
argumentos nomeados. Chame a função com as informações necessárias e dois outros pares nome-valor,
como uma cor ou um recurso opcional. Sua função deve funcionar mais ou menos assim:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Exiba o dicionário retornado para garantir que todas as informações foram corretamente armazenadas.
"""

def make_car(fabricante, modelo, **info_car):
    info_car['fabricante'] = fabricante
    info_car['modelo'] = modelo
    return info_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
