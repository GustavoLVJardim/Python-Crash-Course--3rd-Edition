"""Sem pastrami: Usando a lista 'sandwich_orders' do exercício anterior, assegure-se
de que o 'sanduíche de pastrami' apareça na lista pelo menos três vezes. Faça mais um
código perto do início de seu programa, exibindo uma mensagem que informe que a lanchonete
está sem pastrami e, em seguida, use um loop while para remover todas as ocorrências de
'pastrami' em 'sandwich_orders'. Faça questão de que nenhum sanduíche de pastrami acabe
em 'finished_sandwiches'.
"""
sandwich_orders = ['X-tudo', 'sanduíche de pastrami', 'X-bacon', 'X-salada', 'sanduíche de pastrami', 'X-especial', 'sanduíche de pastrami']

finished_sandwiches = []

print("A lanchonete está sem pastrami. I'm so sorry :(")
while 'sanduíche de pastrami' in sandwich_orders:
    sandwich_orders.remove('sanduíche de pastrami')


while sandwich_orders:
    sanduiche_atual = sandwich_orders.pop()
    finished_sandwiches.append(sanduiche_atual)
    
print('nosso cardápio hoje é:')
for _ in finished_sandwiches:
    print(_)


        