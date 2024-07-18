"""Lanchonete: Crie uma lista chamada 'sandwich_orders' e a preencha
com o nome de diversos sanduíches. Depois, crie uma lista vazia chamada
'finished_sandwiches'. Percorra a lista de pedidos de sanduíches com um
loop e exiba uma mensagem para cada pedido, como: 'Seu lanche de atum está pronto'.
Conforme cada sanduíche é preparado, passe-os para a lista de sanduiches prontos.
Após todos os sanduíches terem sido preparados, exiba uma mensagem enumerando cada um deles.
"""

sandwich_orders = ['X-tudo', 'X-bacon', 'X-salada', 'X-especial']
finished_sandwiches = []

for x in sandwich_orders:
    print(f' Seu {x} está pronto')
    finished_sandwiches.append(x)
    print(finished_sandwiches)

for x in enumerate(finished_sandwiches):
    print(x)